# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from .xixunyun import xixunyun
from app.models import Users
from datetime import datetime, timedelta

# Create your views here.

def index(request):
    return render(request, "index.html")

def select(request):
    if request.method == 'POST':
        studentid = request.POST['studentid']
        password = request.POST['password']
        schoolid = request.POST['schoolid']
        student = xixunyun()
        if student.login_xixun(studentid, password, schoolid):
            return HttpResponse(student.get_history())
        else:
            return HttpResponse("")
    else:
        return HttpResponse("error get")

def insert(request):
    if request.method == 'POST':
        studentid = request.POST['studentid']
        password = request.POST['password']
        schoolid = request.POST['schoolid']
        address = request.POST['address']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        if studentid=="" or password=="" or schoolid =="" or address=="" or latitude=="" or longitude=="":
            return HttpResponse("10001")
        if len(Users.objects.filter(studentid__iexact=studentid).values_list()) != 0:
            return HttpResponse("10002")
        new_user = Users(studentid=studentid, password=password, schoolid=schoolid, address=address, latitude=latitude, longitude=longitude)
        new_user.save()
        if len(Users.objects.filter(studentid__iexact=studentid).values_list()) != 0:
            return HttpResponse("10000")
        else:
            return HttpResponse("10003")

def startapp(request):
    from app.xixunyun import xixunyun
    xxy = xixunyun()
    xxy.run()
    return HttpResponse("Start...")