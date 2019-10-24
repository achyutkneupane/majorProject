from django.http import HttpResponse
from django.shortcuts import render
from .forms import fieldForm
import serial
import psycopg2
from datetime import datetime

def homepage(request):
    return render(request, 'index.html')

def storesField(request):
    conn = psycopg2.connect("host=localhost dbname=postgres user=achyut password=neupane1")
    cur = conn.cursor()
    now = datetime.now()
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
    conn.commit()
    return render(request, 'index.html')