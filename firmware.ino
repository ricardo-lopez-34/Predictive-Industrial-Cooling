#include <WiFi.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <HTTPClient.h>

const int oneWireBus = 4;
const int fanPin = 5;

OneWire oneWire(oneWireBus);
DallasTemperature sensors(&oneWire);

String ssid = ""; String pass = "";

void getWifi() {
  Serial.println("\n--- Cooling System Config ---");
  Serial.println("SSID:"); while (Serial.available() == 0) {}
  ssid = Serial.readStringUntil('\n'); ssid.trim();
  Serial.println("Password:"); while (Serial.available() == 0) {}
  pass = Serial.readStringUntil('\n'); pass.trim();
}

void setup() {
  Serial.begin(115200);
  sensors.begin();
  pinMode(fanPin, OUTPUT);
  getWifi();
  WiFi.begin(ssid.c_str(), pass.c_str());
  while (WiFi.status() != WL_CONNECTED) { delay(500); Serial.print("."); }
}

void loop() {
  sensors.requestTemperatures();
  float t = sensors.getTempCByIndex(0);
  int fanSpeed = (t > 40) ? 255 : (t > 30 ? 128 : 0);
  analogWrite(fanPin, fanSpeed);

  HTTPClient http;
  http.begin("http://your-cooling-app.com/update");
  http.addHeader("Content-Type", "application/json");
  String json = "{\"t\":" + String(t) + ",\"fan\":" + String(fanSpeed) + "}";
  http.POST(json);
  http.end();
  delay(2000);
}
