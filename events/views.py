from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from django.views.generic import ListView
# Create your views here.
#Views funtion based
def HomePage(request):
    return HttpResponse('<h1>Hello from home page</h1>')

def ListEvent(request):
    list =Event.objects.filter(state=True)
    return render(request,'events/EventList.html' , {'events' : list})


#Views Class Based

class ListEventView(ListView):
    model =Event
    template_name ="events/EventList.html"
    context_object_name ="events"
    def get_queryset(self):
        return Event.objects.filter(state=True)
    