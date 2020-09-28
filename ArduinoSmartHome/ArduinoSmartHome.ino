void setup()
{
pinMode(12, OUTPUT);
pinMode(11, OUTPUT);
pinMode(7, OUTPUT);
pinMode(2, INPUT);
Serial.begin(9600);
}
void loop()
{
if(digitalRead(2)==HIGH) {
Serial.println("alert");
digitalWrite(12, HIGH);
digitalWrite(11, LOW);
tone(7, 1000, 500);
delay(500);
digitalWrite(12, LOW);
digitalWrite(11, HIGH);
tone(7, 800, 500);
delay(500);
}
else {
Serial.println("normal");
digitalWrite(12, LOW);
digitalWrite(11, LOW);
delay(1000);
}
}
