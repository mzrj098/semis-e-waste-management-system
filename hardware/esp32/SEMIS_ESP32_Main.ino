#include <WiFi.h>
#include <PubSubClient.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include "config.h"

// Global objects
WiFiClient espClient;
PubSubClient mqtt(espClient);
OneWire oneWire(TEMP_PIN);
DallasTemperature sensors(&oneWire);

void setup() {
  Serial.begin(115200);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  sensors.begin();

  // Connect to WiFi
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to WiFi...");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi Connected!");

  // Connect to MQTT
  mqtt.setServer(MQTT_BROKER, MQTT_PORT);
  reconnectMQTT();
}

void loop() {
  if (!mqtt.connected()) reconnectMQTT();
  mqtt.loop();

  static unsigned long lastReading = 0;
  if (millis() - lastReading >= READING_INTERVAL) {
    lastReading = millis();

    float fillPercent = getFillPercentage();
    float temperature = getTemperature();

    char jsonBuffer[128];
    snprintf(jsonBuffer, sizeof(jsonBuffer),
             "{\"f\":%.1f,\"t\":%.1f,\"ts\":%lu}",
             fillPercent, temperature, millis());

    Serial.printf("Sending: %s\n", jsonBuffer);

    bool success = mqtt.publish(MQTT_TOPIC, jsonBuffer, MQTT_QOS);
    Serial.println(success ? "Message sent successfully" : "Failed to send");
  }
}

// ====================== Helper Functions ======================
float getFillPercentage() {
  float sum = 0;
  for (int i = 0; i < AVERAGE_READINGS; i++) {
    digitalWrite(TRIG_PIN, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG_PIN, LOW);

    long duration = pulseIn(ECHO_PIN, HIGH);
    float distance = duration * 0.0343 / 2;
    sum += distance;
    delay(50);
  }
  float avgDistance = sum / AVERAGE_READINGS;
  float fillPercent = ((BIN_HEIGHT_CM - avgDistance) / BIN_HEIGHT_CM) * 100;
  return constrain(fillPercent, 0, 100);
}

float getTemperature() {
  sensors.requestTemperatures();
  return sensors.getTempCByIndex(0);
}

void reconnectMQTT() {
  while (!mqtt.connected()) {
    Serial.print("Connecting to MQTT...");
    if (mqtt.connect(MQTT_CLIENT_ID)) {
      Serial.println("MQTT Connected");
    } else {
      Serial.print("Failed, rc=");
      Serial.print(mqtt.state());
      delay(5000);
    }
  }
}
Added SEMIS_ESP32_Main.ino - main ESP32 code
