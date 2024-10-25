int i, pot;
float volt;

void setup() {
  Serial.begin(9600); 
  analogReference(DEFAULT);
  pinMode(LED_BUILTIN, OUTPUT);
  i=0;
  delay(10000);
  Serial.println("Indice,Voltagem");
}

void loop() {
  pot = analogRead(A0);
  volt = (pot*50.0)/1023;
  Serial.print(i);
  Serial.print(",");
  Serial.println(volt,3);
  i ++;
  delay(100);
}
