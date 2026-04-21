def preprocess_data(raw_data):
    """Clean the sensor data (matches Chapter 4.2 in thesis)"""
    
    fill_percent = raw_data.get("f", 0.0)
    temperature = raw_data.get("t", 25.0)

    # Simple risk level
    risk_level = "normal"
    if temperature > 45:
        risk_level = "high"

    clean_data = {
        "bin_id": "001",
        "fill_percent": round(fill_percent, 1),
        "temperature": round(temperature, 1),
        "risk_level": risk_level,
        "timestamp": "CURRENT_TIMESTAMP"
    }
    
    print(f"✅ Preprocessed data: {clean_data}")
    return clean_data
