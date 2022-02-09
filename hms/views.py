from django.http.response import HttpResponse
from django.shortcuts import render , HttpResponse
from hms.models import data
from django.contrib import messages 
# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    return render(request,'register.html')
def sdetails(request):
    if request.method == "POST":
        name=request.POST.get('name')
        sex=request.POST.get('sex')
        doctor_name=request.POST.get('doctor_name')
        disease=request.POST.get('disease')
        age=request.POST.get('age')
        blood_group=request.POST.get('blood_group')
        mail=request.POST.get('mail')
        Data=data(name=name,sex=sex,doctor_name=doctor_name,disease=disease,age=age,blood_group=blood_group,mail=mail)
        Data.save()
        messages.success(request, 'Patient Registered Successfully')
    return render(request,'register.html')
