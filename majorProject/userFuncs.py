import serial
import psycopg2
from datetime import datetime
import serial.tools.list_ports
from django import forms
import views

class fieldForm(forms.Form):
   fone = forms.CharField(max_length = 10)
   ftwo = forms.CharField(max_length = 10)
   fthree = forms.CharField(max_length = 10)
   ffour = forms.CharField(max_length = 10)
   ffive = forms.CharField(max_length = 10)
   fsix = forms.CharField(max_length = 10)


def getSensor():
    try:
        conn = psycopg2.connect("host=localhost dbname=postgres user=achyut password=neupane1")
        cur = conn.cursor()
        views.sensorFunc()
        cur.execute("SELECT tempr,hum FROM sensor ORDER BY id DESC LIMIT 1")
        sensor = cur.fetchall()
        for data in sensor:
            senData = "Temperature: " + data[0] + " Humidity: " + data[1] + "\n Soil Moisture: " + data[2]
        return senData
        conn.commit()
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