
bool motorRunning = false;
int spi=13;
int spin=12;
int oo=27;
int oop=26;
int sho=19;
int shot=21;
int op=25;
int ope=33;
int spee=5;
int speed=18;

void setup() {
  // Initialize the LED pin as an output
  pinMode(spi, OUTPUT);
  pinMode(spin, OUTPUT);
  pinMode(oo, OUTPUT);
  pinMode(oop, OUTPUT);
  pinMode(sho, OUTPUT);
  pinMode(shot, OUTPUT);
  pinMode(spee,OUTPUT);
  pinMode(speed,OUTPUT);
  pinMode(op,OUTPUT);
  pinMode(ope,OUTPUT);
  Serial.begin(115200);


}

void loop() {
  if(Serial.available()>0){  
    String input=Serial.readString();
    if (motorRunning == false){
      if(input=="nomal" ){
        motorRunning = true;
        digitalWrite(spi,LOW);
        digitalWrite(spin,LOW);
        digitalWrite(op,LOW);
        digitalWrite(ope,HIGH);
        delay(250);
        digitalWrite(op,LOW);
        digitalWrite(ope,LOW);
        delay(100);
        digitalWrite(sho,LOW);
        digitalWrite(shot,HIGH);
        delay(100);
        digitalWrite(sho,LOW);
        digitalWrite(shot,LOW);
        digitalWrite(op,HIGH);
        digitalWrite(ope,LOW);
        delay(250);
        digitalWrite(op,LOW);
        digitalWrite(ope,LOW);
        delay(100);
        digitalWrite(sho,HIGH);
        digitalWrite(shot,LOW);
        delay(100);
        digitalWrite(sho,LOW);
        digitalWrite(shot,LOW);
        motorRunning = false;
        Serial.println("done"); 
      }
      else if(input=="up" ){
        motorRunning = true;
        digitalWrite(spi,LOW);
        digitalWrite(spin,LOW);
        analogWrite(speed, 250);
        digitalWrite(oo,LOW);
        digitalWrite(oop,HIGH);
        delay(500);
        analogWrite(speed, 250);
        digitalWrite(oo,LOW);
        digitalWrite(oop,LOW);
        delay(100);
        digitalWrite(op,LOW);
        digitalWrite(ope,HIGH);
        delay(250);
        digitalWrite(op,LOW);
        digitalWrite(ope,LOW);
        delay(100);
        digitalWrite(sho,LOW);
        digitalWrite(shot,HIGH);
        delay(100);
        digitalWrite(sho,LOW);
        digitalWrite(shot,LOW);
        digitalWrite(sho,HIGH);
        digitalWrite(shot,LOW);
        delay(100);
        digitalWrite(sho,LOW);
        digitalWrite(shot,LOW);
        digitalWrite(op,HIGH);
        digitalWrite(ope,LOW);
        delay(250);
        digitalWrite(op,LOW);
        digitalWrite(ope,LOW);
        motorRunning = false;
        Serial.println("done"); 
      }
      else if(input=="down" ){
        motorRunning = true;
        digitalWrite(spi,LOW);
        digitalWrite(spin,LOW);
        analogWrite(speed, 250);
        digitalWrite(oo,HIGH);
        digitalWrite(oop,LOW);
        delay(500);
        analogWrite(speed, 250);
        digitalWrite(oo,LOW);
        digitalWrite(oop,LOW);
        delay(100);
        digitalWrite(op,LOW);
        digitalWrite(ope,HIGH);
        delay(250);
        digitalWrite(op,LOW);
        digitalWrite(ope,LOW);
        delay(100);
        digitalWrite(sho,LOW);
        digitalWrite(shot,HIGH);
        delay(100);
        digitalWrite(sho,LOW);
        digitalWrite(shot,LOW);
        digitalWrite(sho,HIGH);
        digitalWrite(shot,LOW);
        delay(100);
        digitalWrite(sho,LOW);
        digitalWrite(shot,LOW);
        digitalWrite(op,HIGH);
        digitalWrite(ope,LOW);
        delay(250);
        digitalWrite(op,LOW);
        digitalWrite(ope,LOW);
        motorRunning = false;
        Serial.println("done"); 
      } 
      else if(input=="go" ){
        motorRunning = true;
        analogWrite(spee, 250);
        digitalWrite(spi,LOW);
        digitalWrite(spin,HIGH);
        delay(100);
        analogWrite(spee, 0);
        digitalWrite(spi,LOW);
        digitalWrite(spin,LOW);
        delay(1000);
        motorRunning = false;
        Serial.println("done");
      }
      else if(input=="stop"){
        motorRunning = true;
        digitalWrite(spi,LOW);
        digitalWrite(spin,LOW);
        motorRunning = false;
        Serial.println("done");
      }
      else if(input=="back"){
        motorRunning = true;
        analogWrite(spee, 250);
        digitalWrite(spi,HIGH);
        digitalWrite(spin,LOW);
        delay(100);
        analogWrite(spee, 0);
        digitalWrite(spi,LOW);
        digitalWrite(spin,LOW);
        delay(1000);
        motorRunning = false;
        Serial.println("done");
      }
    }
  }
}
