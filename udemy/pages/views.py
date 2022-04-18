from django.shortcuts import render
from django.http import HttpResponse

# from udemy.cars.models import Cars
from .models import Team
from cars.models import Car


def home(request):
    teams  = Team.objects.all()
    featured_cars = Car.object.order_by("-created_date").filter(is_featured = True)
    
    data = {
        'teams' : teams,
        'featured_cars':featured_cars,
    }
    
    return render (request,'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams' : teams,
    }
    return render (request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contacts(request):
    return render (request,'pages/contact.html')