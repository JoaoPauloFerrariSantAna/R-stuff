//waste of funcking time!!!

#include <WiFi.h>
#include <HTTPClient.h>

#define WIFI_NAME "HOMERSIMPSON"
#define WIFI_PASS "4D2A1BC2"

HTTPClient http;

int soil_moisture = 4;
int response_code = 0;
String server_path = "https://jsonplaceholder.typicode.com/comments";

void setup() {
  Serial.begin(9600);
  
  WiFi.begin(WIFI_NAME, WIFI_PASS);

  while(WiFi.status() != WL_CONNECTED) {};

  Serial.print("Connected to: ");
  Serial.println(WiFi.localIP()); 
}

void loop() {
  if(WiFi.status() == WL_CONNECTED) {
    http.begin(server_path.c_str());

    response_code = http.GET();
    
    if (response_code > 0) {
        String payload = http.getString();
        
        Serial.println(payload);
    } else {
      Serial.print("Error code: ");
      Serial.println(response_code);
    }

    http.end();
  } else {
      Serial.println("WiFi Disconnected");
  }
}
