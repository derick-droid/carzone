
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('about',views.about, name="about"),
    path('services',views.services,name = "services"),
    path('contacts',views.contacts,name="contacts")
    
]