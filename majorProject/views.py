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
from team.models import Member
from django.http import StreamingHttpResponse
from camera import VideoCamera, gen

arduino = '/dev/ttyACM0'

def homepage(request):
    getSenText = getSensor()
    getFlText = fieldData()
    members = Member.objects.all().values()
    context = {
        'team':members,
        'text': getSenText,
        'ftext': getFlText,
        'project': 'Project Name'
    }
    return render(request, 'index.html', context= context)

def storesField(request):
    conn = psycopg2.connect("host=localhost dbname=postgres user=achyut password=neupane1")
    cur = conn.cursor()
    now = datetime.now()
    ser = serial.Serial(arduino, 9600)
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
            """ fone = fone*10+1
            ftwo = ftwo*10+2
            fthree = fthree*10+3
            ffour = ffour*10+4
            ffive = ffive*10+5
            fsix = fsix*10+6 """
            ser.write(fone.encode())
            ser.write(ftwo.encode())
            ser.write(fthree.encode())
            ser.write(ffour.encode())
            ser.write(ffive.encode())
            ser.write(fsix.encode())
            conn.commit()
    return render(request, 'redirect_to_home.html')

def stopF(request):
    conn = psycopg2.connect("host=localhost dbname=postgres user=achyut password=neupane1")
    cur = conn.cursor()
    now = datetime.now()
    getSenText = getSensor()
    getFlText = fieldData()
    cur.execute("UPDATE field SET op = 'stopped'")
    conn.commit()
    return render(request, 'redirect_to_home.html')

def sensorUp(request):
    getSenText = getSensor()
    return render(request, 'data.html', {'text': getSenText})

def camera(request):
    cameraa = StreamingHttpResponse(gen(VideoCamera()),content_type='multipart/x-mixed-replace; boundary=frame')
    try:
        return cameraa
    except AttributeError:
        pass