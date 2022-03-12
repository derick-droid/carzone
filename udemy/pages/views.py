from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render (request,'pages/home.html')

def about(request):
    return render (request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services.html')

def contacts(request):
    return render (request,'pages/contact.html')