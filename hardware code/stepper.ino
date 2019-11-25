#include <string.h>
int a[2],n=0,value;
void setup() {
Serial.begin(9600);
Serial.println("Enter\n");
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
  case 1:
    y=1200;
    break;
  case 2:
    y=0;
    break;
  case 3:
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
    case 1:
    x=-1200;
    y=1200;
    break;
    case 2:
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
    case 5:
    x=-1200;
    y=-1200;
    break;
    case 6:
    x=-2600;
    y=-1200;
    break;
  }
  move(x,y,1200);
    Serial.print("Planted in: ");
    Serial.println(f);
}

void move(int x,int y,int z) {
   Serial.print("x:");
   Serial.println(x);
   delay(10);
   Serial.print("y:");
   Serial.println(y);
   delay(10);
   Serial.print("z:");
   Serial.println(z);
   delay(10);
   Serial.print("z:");
   Serial.println(-z);
   delay(10);
   Serial.print("y:");
   Serial.println(-y);
   delay(10);
   Serial.print("x:");
   Serial.println(-x);
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
