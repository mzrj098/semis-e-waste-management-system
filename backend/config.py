import os
from dotenv import load_dotenv

load_dotenv()

# MQTT Settings
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "semis/ewaste/bin/001"
MQTT_QOS = 1

# MySQL Database Settings
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "your_password_here"     # ← Change this later to your real MySQL password
DB_NAME = "semis_ewaste"

# Secret key for Flask
SECRET_KEY = "semis-secret-key-2026"
