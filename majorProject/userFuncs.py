import serial
import psycopg2
from datetime import datetime
import serial.tools.list_ports
from django import forms

class fieldForm(forms.Form):
   fone = forms.CharField(max_length = 10)
   ftwo = forms.CharField(max_length = 10)
   fthree = forms.CharField(max_length = 10)
   ffour = forms.CharField(max_length = 10)
   ffive = forms.CharField(max_length = 10)
   fsix = forms.CharField(max_length = 10)

conn = psycopg2.connect("host=localhost dbname=postgres user=achyut password=neupane1")
cur = conn.cursor()
now = datetime.now()
ser = serial.Serial('/dev/ttyACM0', 9600)

def sensorFunc():
    try:
        line = ser.readline()
        conn.commit()
        x = line.split(" ")
        tempr = int(round(float(x[0])))
        hum = int(round(float(x[1])))
        if(0<=tempr<=50 and 20<=hum<=90):
            cur.execute("insert into sensor(tempr,hum,time) values(%s,%s,%s)", (tempr,hum,now))
    except serial.serialutil.SerialException:
        pass
    except IndexError:
        pass
    except ValueError:
        pass
    except TypeError:
        pass
    except UnboundLocalError:
        pass

def getSensor():
    sensorFunc()
    cur.execute("SELECT tempr,hum FROM sensor ORDER BY id DESC LIMIT 1")
    sensor = cur.fetchall()
    for data in sensor:
        senData = "Temperature: " + data[0] + " Humidity: " + data[1]
    return senData