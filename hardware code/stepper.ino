#include <string.h>
#include <Stepper.h>
int a[2],n=0,value;
const int steps=200;
Stepper sx(steps,8,9,10,13);
Stepper sy(steps,14,15,16,17);
Stepper sz(steps,23,25,27,29);
void setup() {
Serial.begin(9600);
pinMode(11,OUTPUT);
pinMode(12,OUTPUT);
pinMode(23,OUTPUT);
pinMode(24,OUTPUT);
pinMode(35,OUTPUT);
pinMode(36,OUTPUT);
pinMode(3,INPUT);
pinMode(4,INPUT);
pinMode(5,INPUT);
sx.setSpeed(80);
sy.setSpeed(80);
sz.setSpeed(100);
}

void loop() {
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
    move(0,y,1200);
    Serial.print("Picked from: ");
    Serial.println(s);
}

void plantSeed(int f) {
  int x,y;
  switch(f) {
    case 5:
    x=-1200;
    y=1200;
    break;
    case 6:
    x=-2600;
    y=1200;
    break;
    case 3:
    x=-1200;
    y=0;
    break;
    case 4:
    x=-2600;
    y=0;
    break;
    case 1:
    x=-1200;
    y=-1200;
    break;
    case 2:
    x=-2600;
    y=-1200;
    break;
  }
  move(x,y,1200);
    Serial.print("Planted in: ");
    Serial.println(f);
}

void move(int x,int y,int z) {
   sx.step(x);
   delay(10);
   sy.step(y);
   delay(10);
   sz.step(z);
   delay(10);
   sz.step(-z);
   delay(10);
   sy.step(-y);
   delay(10);
   sx.step(-x);
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
