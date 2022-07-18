from asyncio.windows_events import NULL
from ctypes import sizeof
from os import link
import re
from unicodedata import name
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from hms.models import data
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'register.html')


def view(request):
    if request.method == "POST":
        nm = request.POST.get('id')
        if nm == '':
            link = '/view'
            messages.success(request, 'Blank Input')
            return render(request, 'message.html', {link: 'link'})
        db = data.objects.filter(firstName=nm)
        if bool(db):
            disp = "flex"
            return render(request, 'data.html', {'db': db, 'display': disp})
        else:
            link = '/view'
            messages.success(request, 'No Patient Found')
            return render(request, 'message.html', {link: 'link'})
    else:
        disp = "none"
        return render(request, 'data.html', {'display': disp})


def delete_view(request):
    if request.method == "POST":
        nm = request.POST.get('id')
        db = data.objects.filter(firstName=nm)
        if bool(db):
            disp = "flex"
            return render(request, 'delete.html', {'db': db, 'display': disp, 'nm': nm})
        else:
            link = '/delete_view'
            messages.success(request, 'No Patient Found')
            return render(request, 'message.html', {link: 'link'})
    else:
        disp = "none"
        return render(request, 'delete.html', {'display': disp})


def deleteBtn(request):
    if request.method == "POST":
        nm = request.POST.get('identity')
        print(nm)
        db = data.objects.filter(firstName=nm)
        print(db)
        data.objects.filter(firstName=nm).delete()
        db.delete()
        messages.success(request, 'Patient discharged Successfully')
        link = '/home'
        return render(request, 'message.html', {'link': link})
    else:
        return render(request, 'index.html')


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
        link = '/home'
        return render(request, 'message.html', {'link': link})
