
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('offer.html', views.offer, name='offer'),
    path('appointment.html', views.appointment, name='appointment')

]
