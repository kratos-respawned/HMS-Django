from asyncio.windows_events import NULL
from ctypes import sizeof
from unicodedata import name
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from hms.models import data
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'register.html')


def sed(request):
    return render(request, 'coming_soon.html')


def view(request):
    if request.method == "POST":
        nm = request.POST.get('id')
        if nm == '':
            return render(request, 'data.html')
        db = data.objects.filter(firstName=nm)
        if bool(db):
            disp = "flex"
            return render(request, 'data.html', {'db': db, 'display': disp})
        # data.objects.filter(name=nm).delete()
        # return render(request,'data.html',{'db':db})
        else:
            return render(request, 'data.html')
    else:
        disp = "none"
        return render(request, 'data.html', {'display': disp})


def sdetails(request):
    if request.method == "POST":
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        disease = request.POST.get('disease')
        phoneNumber = request.POST.get('tel')
        bloodGroup = request.POST.get('bloodGroup')
        doctorsName = request.POST.get('doctorsName')
        Data = data(firstName=firstName, lastName=lastName, age=age, sex=sex, disease=disease,
                    phoneNumber=phoneNumber, bloodGroup=bloodGroup, doctorsName=doctorsName)
        Data.save()
        messages.success(request, 'Patient Registered Successfully')
    return render(request, 'register.html')
