from django.http import HttpResponse
from django.shortcuts import render
from .userFuncs import fieldForm
from .userFuncs import sensorFunc
from .userFuncs import getSensor
from .userFuncs import fieldData
import serial
import psycopg2
from datetime import datetime
import serial.tools.list_ports

arduino = '/dev/ttyACM0'

def homepage(request):
    getSenText = getSensor()
    getFlText = fieldData()
    return render(request, 'index.html', {'text': getSenText, 'ftext': getFlText})

def storesField(request):
    conn = psycopg2.connect("host=localhost dbname=postgres user=achyut password=neupane1")
    cur = conn.cursor()
    now = datetime.now()
    getSenText = getSensor()
    getFlText = fieldData()
    if request.method == "POST":
        fieldsForm = fieldForm(request.POST)
        check = fieldsForm.is_valid()
        if fieldsForm.is_valid(): 
            fone = fieldsForm.cleaned_data['fone']
            ftwo = fieldsForm.cleaned_data['ftwo']
            fthree = fieldsForm.cleaned_data['fthree']
            ffour = fieldsForm.cleaned_data['ffour']
            ffive = fieldsForm.cleaned_data['ffive']
            fsix = fieldsForm.cleaned_data['fsix']
            cur.execute("insert into field(fone,ftwo,fthree,ffour,ffive,fsix,time,op) values(%s,%s,%s,%s,%s,%s,%s,%s)", (fone,ftwo,fthree,ffour,ffive,fsix,now,'running'))
            ser.write(fone.encode() + " " + ftwo.encode() + " " + fthree.encode() + " " + ffour.encode() + " " + ffive.encode() + " " + fsix.encode())
            conn.commit()
    return render(request, 'redirect_to_home.html', {'text': getSenText, 'ftext': getFlText})

def stopF(request):
    conn = psycopg2.connect("host=localhost dbname=postgres user=achyut password=neupane1")
    cur = conn.cursor()
    now = datetime.now()
    getSenText = getSensor()
    getFlText = fieldData()
    cur.execute("UPDATE field SET op = 'stopped'")
    conn.commit()
    return render(request, 'redirect_to_home.html', {'text': getSenText, 'ftext': getFlText})

def sensorUp(request):
    getSenText = getSensor()
    return render(request, 'data.html', {'text': getSenText})