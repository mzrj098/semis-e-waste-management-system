import paho.mqtt.client as mqtt
import json
from config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC
from data_preprocessor import preprocess_data
from db_manager import save_to_database

def on_connect(client, userdata, flags, rc):
    print("✅ Connected to MQTT broker")
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        print(f"📨 Received from bin: {payload}")

        clean_data = preprocess_data(payload)
        save_to_database(clean_data)

    except Exception as e:
        print(f"❌ Error: {e}")

# Create MQTT Client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_forever()
