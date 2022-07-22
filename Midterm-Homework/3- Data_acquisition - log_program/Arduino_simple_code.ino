#include <MPU6050.h>
#include <Wire.h>

MPU6050 MPU;

int ivmeX , ivmeY , ivmeZ , GyroX , GyroY , GyroZ;


void setup() {

  Serial.begin(9600);
  Wire.begin();
  MPU.initialize();

}

void loop() {

  MPU.getAcceleration(&ivmeX, &ivmeY, &ivmeZ);
  MPU.getRotation(&GyroX, &GyroY, &GyroZ);
  
  Serial.print(ivmeX);
  Serial.print(" ");  
  Serial.print(ivmeY);
  Serial.print(" ");  
  Serial.print(ivmeZ);
  Serial.print(" ");
  Serial.print(GyroX);
  Serial.print(" ");  
  Serial.print(GyroY);
  Serial.print(" ");  
  Serial.print(GyroZ);
  Serial.print(" ");
  
  int Serial_1 = analogRead(A0);
  Serial.print(Serial_1);
  Serial.print(" "); 
  int Serial_2 = analogRead(A1);
  Serial.println(Serial_2);
  
  delay(150);

}
