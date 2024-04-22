#include <HTTPClient.h>
//#include <WiFiClientSecure.h>
#include <WiFi.h>

#define WIFI_NAME "HOMERSIMPSON"
#define WIFI_PASSWORD "4D2A1BC2"

//String moisture = "413";
String postData = " ";

void setup() {
  Serial.begin(9600);

  WiFi.begin(WIFI_NAME, WIFI_PASSWORD);

  while (WiFi.status() != WL_CONNECTED) {}

  Serial.println(WiFi.localIP());
}

void loop() {
  HTTPClient http;    //Declare object of class HTTPClient

//  String host_name = "http://192.168.1.109/";
//  String path_name = "teste2.php";
  String query_string = "umidade=777";
  
  http.begin("http://192.168.1.109/teste2.php");              //change the ip to your computer ip address
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");    //Specify content-type header
 
  int httpCode = http.POST(query_string);   //Send the request
  String payload = http.getString();    //Get the response payload
 
  Serial.println(httpCode);   //Print HTTP return code
  Serial.println(payload);    //Print request response payload
 
  http.end();  //Close connection
}
