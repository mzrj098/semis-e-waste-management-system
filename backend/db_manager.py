import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
from rule_based_classifier import classify_waste

def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

def save_to_database(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    waste_type = classify_waste(data["fill_percent"], data["temperature"])

    sql = """
    INSERT INTO sensor_data 
    (bin_id, fill_percent, temperature, risk_level, waste_type, green_score)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    green_score = round(data["fill_percent"] * 0.8, 1)   # Simple green score

    values = (
        data["bin_id"],
        data["fill_percent"],
        data["temperature"],
        data["risk_level"],
        waste_type,
        green_score
    )

    cursor.execute(sql, values)
    conn.commit()
    print(f"💾 Saved to DB - Waste Type: {waste_type} | Green Score: {green_score}")

    cursor.close()
    conn.close()
