#define AOUT_PIN A0 // Arduino pin that connects to AOUT pin of moisture sensor
int RELAY_PIN = 6;

const int OpenAirReading = 592;   //calibration data 1
const int WaterReading = 287;     //calibration data 2
int MoistureLevel = 0;
int SoilMoisturePercentage = 0;

void setup() {
  Serial.begin(9600);
  pinMode(RELAY_PIN, OUTPUT);
}

void loop() {
  MoistureLevel = analogRead(AOUT_PIN);
  //MoistureLevel = analogRead(A0);  //update based on the analog Pin selected
  //Serial.println(soilMoistureValue);
  SoilMoisturePercentage = map(MoistureLevel, OpenAirReading, WaterReading, 0, 100);
 
  if (SoilMoisturePercentage >= 100)
  {
    Serial.println("100");
  }
  else if (SoilMoisturePercentage <= 0)
  {
    Serial.println("0");
  }
  else if (SoilMoisturePercentage > 0 && SoilMoisturePercentage < 100)
  {
    Serial.println(SoilMoisturePercentage);
    //Serial.println("%");
  }
  
  //Serial.println(MoistureLevel);

  if (Serial.available()) {  // check for incoming serial data
      String command = Serial.readString();  // read command from serial port
      if (command == "led_on") {  // turn on LED
         digitalWrite(RELAY_PIN, LOW);
         } 
      else if (command == "led_off") {  // turn off LED
         digitalWrite(RELAY_PIN, HIGH);
      }
  /*    
else if (command == "read_a0") {  // read and send A0 analog value
      if (SoilMoisturePercentage >= 100)
  {
    Serial.println("100");
  }
  else if (SoilMoisturePercentage <= 0)
  {
    Serial.println("0");
  }
  else if (SoilMoisturePercentage > 0 && SoilMoisturePercentage < 100)
  {
    Serial.println(SoilMoisturePercentage);
    //Serial.println("%");
  }
  
      }

      */
}
delay(500);
}
