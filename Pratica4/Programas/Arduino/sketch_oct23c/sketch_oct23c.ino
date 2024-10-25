int i, pot;
float volt;

void setup() {
  Serial.begin(9600); 
  analogReference(DEFAULT);
}

void loop() {
  Serial.println("CLEARDATA");
  Serial.println("LABEL,Ponto,Volts");

  for(i=0; i<515; i++)
  {
    Serial.print("DATA, ");
    pot = analogRead(A0);
    volt = (pot*50.0)/1023;
    Serial.print(i);
    Serial.print(",");
    Serial.println(volt,2);
    delay(200); // Em ms
  }
  exit(0);
}
