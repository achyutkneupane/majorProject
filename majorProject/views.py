from django.http import HttpResponse
from django.shortcuts import render
from .userFuncs import fieldForm
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
        if fieldsForm.is_valid(): 
            fone = fieldsForm.cleaned_data['fone']
            ftwo = fieldsForm.cleaned_data['ftwo']
            fthree = fieldsForm.cleaned_data['fthree']
            ffour = fieldsForm.cleaned_data['ffour']
            ffive = fieldsForm.cleaned_data['ffive']
            fsix = fieldsForm.cleaned_data['fsix']
            ser.write(fone.encode())
            ser.write('1')
            ser.write(ftwo.encode())
            ser.write('2')
            ser.write(fthree.encode())
            ser.write('3')
            ser.write(ffour.encode())
            ser.write('4')
            ser.write(ffive.encode())
            ser.write('5')
            ser.write(fsix.encode())
            ser.write('6')
            cur.execute("insert into field(fone,ftwo,fthree,ffour,ffive,fsix,time,op) values(%s,%s,%s,%s,%s,%s,%s,%s)", (fone,ftwo,fthree,ffour,ffive,fsix,now,'running'))
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
        mois = int(round(float(x[2])))
        if(0<=tempr<=50 and 20<=hum<=90):
            cur.execute("insert into sensor(tempr,hum,mois,time) values(%s,%s,%s,%s)", (tempr,hum,mois,now))
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

def sensorUp(request):
    getSenText = getSensor()
    return render(request, 'data.html', {'text': getSenText})

def camera(request):
    cameraa = StreamingHttpResponse(gen(VideoCamera()),content_type='multipart/x-mixed-replace; boundary=frame')
    try:
        return cameraa
    except AttributeError:
        pass