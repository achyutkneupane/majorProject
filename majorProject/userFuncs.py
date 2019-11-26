import serial
import psycopg2
from datetime import datetime
import serial.tools.list_ports
from django import forms

arduino = '/dev/ttyACM0'

class fieldForm(forms.Form):
   fone = forms.CharField(max_length = 10)
   ftwo = forms.CharField(max_length = 10)
   fthree = forms.CharField(max_length = 10)
   ffour = forms.CharField(max_length = 10)
   ffive = forms.CharField(max_length = 10)
   fsix = forms.CharField(max_length = 10)

def sensorFunc():
    conn = psycopg2.connect("host=localhost dbname=postgres user=achyut password=neupane1")
    cur = conn.cursor()
    now = datetime.now()
    ser = serial.Serial(arduino, 9600)
    try:
        line = ser.readline()
        x = line.split(" ")
        tempr = int(round(float(x[0])))
        hum = int(round(float(x[1])))
        if(0<=tempr<=50 and 20<=hum<=90):
            cur.execute("insert into sensor(tempr,hum,time) values(%s,%s,%s)", (tempr,hum,now))
            conn.commit()
    except serial.serialutil.SerialException:
        return "Serial Connection Error"
    except IndexError:
        pass
    except ValueError:
        pass
    except TypeError:
        pass
    except UnboundLocalError:
        pass

def getSensor():
    try:
        conn = psycopg2.connect("host=localhost dbname=postgres user=achyut password=neupane1")
        cur = conn.cursor()
        ser = serial.Serial(arduino, 9600)
        sensorFunc()
        cur.execute("SELECT tempr,hum FROM sensor ORDER BY id DESC LIMIT 1")
        sensor = cur.fetchall()
        for data in sensor:
            senData = "Temperature: " + data[0] + " Humidity: " + data[1]
        return senData
        conn.commit()
    except serial.serialutil.SerialException:
        return "Serial Connection Error"
    except UnboundLocalError:
        pass

def fieldData():
    conn = psycopg2.connect("host=localhost dbname=postgres user=achyut password=neupane1")
    cur = conn.cursor()
    fData = '0'
    cur.execute("SELECT * FROM field WHERE op = 'running' ORDER BY id DESC LIMIT 1")
    field = cur.fetchall()
    for data in field:
        if(data[8] == "running"):
            fxData = data[1] + " " + data[2] + " " + data[3] + " " + data[4] + " " + data[5] + " " + data[6]
            fData = fxData.split()
        elif(data[8] == "stopped"):
            fData = '0'
    conn.commit()
    return fData