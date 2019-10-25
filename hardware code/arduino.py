import serial
import psycopg2
from datetime import datetime
conn = psycopg2.connect("host=localhost dbname=postgres user=achyut password=neupane1")
cur = conn.cursor()
now = datetime.now()
test = "125"
ser = serial.Serial('/dev/ttyACM0', 9600)
ser.write(test)
while 1: 
    if(ser.in_waiting >0):
        line = ser.readline()
        cur.execute("insert into keypad(key,time) values(%s,%s)", (line,now))
        conn.commit()
        print(line)