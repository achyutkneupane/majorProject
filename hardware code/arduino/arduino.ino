#include <dht.h>
#include <string.h>
#include <Stepper.h>
#define DHT11_PIN 7
#include <Servo.h>
Servo myservo;
dht DHT;
int a[2],n=0,value,pos=0,soil=A7,water=33;
const int steps=200;
Stepper sx(steps,8,9,10,13);
Stepper sy(steps,14,15,16,17);
Stepper sz(steps,23,25,27,29);
void setup() {
Serial.begin(9600);
myservo.attach(2);
sx.setSpeed(90);
sy.setSpeed(80);
sz.setSpeed(100);
pinMode(soil, INPUT);
pinMode(water,OUTPUT);
}

void loop() {
  sensor();
  if (Serial.available() > 0) {
  value = Serial.read()-48;
  callfunc(value);
}
}

void pickSeed(int s) {
  int y;
switch(s) {
  case 3:
    y=700;
    break;
  case 2:
    y=0;
    break;
  case 1:
    y=-700;
    break;
}
    move(0,y,2300);
    picker();
    movei(0,y,2300);
}

void plantSeed(int f) {
  int x,y;
  switch(f) {
    case 1:
    x=-1000;
    y=-1600;
    break;
    case 2:
    x=-3200;
    y=-1600;
    break;
    case 3:
    x=-1000;
    y=0;
    break;
    case 4:
    x=-3200;
    y=0;
    break;
    case 5:
    x=-1000;
    y=1600;
    break;
    case 6:
    x=-3200;
    y=1600;
    break;
  }
  move(x,y,5000);
  picker();
  movei(x,y,5000);
}

void move(int x,int y,int z) {
   sx.step(x);
   delay(10);
   sy.step(y);
   delay(10);
   sz.step(z);
   delay(10);
}
void movei(int x,int y,int z) {
   sz.step(-z);
   delay(10);
   sy.step(-y);
   delay(10);
   sz.step(-x);
   delay(10);
}

void sensor() {
DHT.read11(DHT11_PIN);
int mois = analogRead(soil);
Serial.print(DHT.temperature);
Serial.print(' ');
Serial.print(DHT.humidity);
Serial.print(' ');
Serial.println(mois);
if(mois <= 300) {
 //waterr();
}
delay(2000);
}

void picker() {
    for (pos = 180; pos >= 0; pos -= 1) { 
    myservo.write(pos);
    delay(15);
    }
    for (pos = 0; pos <= 180; pos += 1) {
    myservo.write(pos); 
    delay(15);
    }
}

void waterr() {
  move(-1000,-1600,5000);
  digitalWrite(water,HIGH);
  delay(10000);
  digitalWrite(water,LOW);
  movei(0,0,1000);
  move(-2200,0,1000);
  digitalWrite(water,HIGH);
  delay(10000);
  digitalWrite(water,LOW);
  movei(0,0,1000);
  move(2200,1600,1000);
  digitalWrite(water,HIGH);
  delay(10000);
  digitalWrite(water,LOW);
  movei(0,0,1000);
  move(-2200,0,1000);
  digitalWrite(water,HIGH);
  delay(10000);
  digitalWrite(water,LOW);
  movei(0,0,1000);
  move(2200,1600,1000);
  digitalWrite(water,HIGH);
  delay(10000);
  digitalWrite(water,LOW);
  movei(0,0,1000);
  move(-2200,0,1000);
  digitalWrite(water,HIGH);
  delay(10000);
  digitalWrite(water,LOW);
  movei(-3200,1600,5000);
}

 void callfunc(int value) {
 int digit = value % 10;
 value /= 10;
 a[n++] = digit;
 if(a[1] >0) {
      pickSeed(a[0]);
      plantSeed(a[1]);
  a[0] = a[1] = n = 0;
 }
}
