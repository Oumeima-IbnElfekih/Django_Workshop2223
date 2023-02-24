from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
# Create your views here.

def HomePage(request):
    return HttpResponse('<h1>Hello from home page</h1>')

def ListEvent(request):
    list =Event.objects.all()
    return render(request,'events/EventList.html' , {'events' : list})