//code obtained from: https://how2electronics.com/interface-capacitive-soil-moisture-sensor-arduino/

#define SENSOR_PIN 36

const int AirValue = 620;   //you need to replace this value with Value_1
const int WaterValue = 310;  //you need to replace this value with Value_2
int soilMoistureValue = 0;
int soilmoisturepercent=0;

void setup() {
  Serial.begin(9600); // open serial port, set the baud rate to 9600 bps
}
void loop() {
soilMoistureValue = analogRead(SENSOR_PIN);  //put Sensor insert into soil

soilmoisturepercent = map(soilMoistureValue, AirValue, WaterValue, 0, 100);

if(soilmoisturepercent >= 100)
{
  Serial.println("100 %");
}
else if(soilmoisturepercent <=0)
{
  Serial.println("0 %");
}
else if(soilmoisturepercent >0 && soilmoisturepercent < 100)
{
  Serial.print(soilmoisturepercent);
  Serial.println("%");
  Serial.println(soilMoistureValue);
}
  delay(250);
}
