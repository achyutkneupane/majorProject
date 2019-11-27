#include <dht.h>
#include <string.h>
#include <Stepper.h>
#define DHT11_PIN 7
#include <Servo.h>
Servo myservo;
dht DHT;
int a[2],n=0,value,pos=0,soil=A7;
const int steps=200;
Stepper sx(steps,8,9,10,13);
Stepper sy(steps,14,15,16,17);
Stepper sz(steps,23,25,27,29);
void setup() {
Serial.begin(9600);
myservo.attach(2);
sx.setSpeed(80);
sy.setSpeed(80);
sz.setSpeed(100);
pinMode(soil, INPUT);
pinMode(33,OUTPUT);
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
    y=1200;
    break;
  case 2:
    y=0;
    break;
  case 1:
    y=-1200;
    break;
}
    move(0,y,2400);
    picker();
    movei(0,y,2400);
}

void plantSeed(int f) {
  int x,y;
  switch(f) {
    case 5:
    x=-1200;
    y=1200;
    break;
    case 6:
    x=-3500;
    y=1200;
    break;
    case 3:
    x=-1200;
    y=0;
    break;
    case 4:
    x=-3500;
    y=0;
    break;
    case 1:
    x=-1200;
    y=-1200;
    break;
    case 2:
    x=-3500;
    y=-1200;
    break;
  }
  move(x,y,6000);
  picker();
  movei(x,y,6000);
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
   sx.step(-z);
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
delay(2000);
}

void picker() {
    for (pos = 0; pos <= 180; pos += 1) {
    myservo.write(pos); 
    delay(15);
    }
    move(0,0,50);
    for (pos = 180; pos >= 0; pos -= 1) { 
    myservo.write(pos);
    delay(15);
    move(0,0,-50);
    }
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
