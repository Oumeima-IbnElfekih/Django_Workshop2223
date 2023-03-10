from django.shortcuts import render ,redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Event,Participation
from datetime import date
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
#Views funtion based
def HomePage(request):
    return HttpResponse('<h1>Hello from home page</h1>')

def ListEvent(request):
    list =Event.objects.filter(state=True)
    return render(request,'events/EventList.html' , {'events' : list})


def add_event(req):
    form =EventForm()
    if req.method =="POST" :
        form =EventForm(req.POST,req.FILES)
        if form.is_valid():
            # print(**form.cleaned_data)
            Event.objects.create(**form.cleaned_data)
            return redirect('list_events_view')
        else:
            print(form.errors)
    return render(req, "events/event_form.html",{'form':form})      

@login_required
def create_event(req):
    if req.method =="GET":
        form =EventModelForm()
        return render(req, "events/event_form.html",{'form':form}) 
    if req.method=="POST":
        form =EventModelForm(req.POST,req.FILES)
        if form.is_valid():
            Event =form.save(commit=False)
            Event.save()
            return redirect('list_events_view')
        else: 
            return render(req, "events/event_form.html",{'form':form}) 
        
#Views Class Based


def participate(req,event_id):
    event=Event.objects.get(id=event_id)
    user=req.user
    if Participation.objects.filter(Person=user,event=event).count() ==0:
        event.nbe_participant+=1
        event.save()
        part=Participation.objects.create(Person=user,event=event,
                                          date_participation=date.today)
        part.save()
        return redirect('list_events_view')
    else:
        return redirect('list_events_view')
    
class ListEventView(LoginRequiredMixin,ListView):
    login_url="login"
    model =Event
    template_name ="events/EventList.html"
    context_object_name ="events"
    # def get_queryset(self):
    #     return Event.objects.filter(state=True)

class DetailEventView(LoginRequiredMixin,DetailView):
    login_url="login"
    model=Event
    template_name ="events/DetailsEvent.html"
    context_object_name ="event"
    
class CreateEvent(LoginRequiredMixin,CreateView):
    login_url="login"
    model=Event
    template_name="events/event_form.html"
    form_class=EventModelForm
    success_url= reverse_lazy('list_events_view')
    def form_valid(self, form):
        form.instance.organizer = Person.objects.get(cin=self.request.user.cin)
        return super().form_valid(form)
    
class UpdateEvent(LoginRequiredMixin,UpdateView):
    model=Event
    template_name="events/event_form.html"
    form_class=EventModelForm
    success_url= reverse_lazy('list_events_view')
    


class DeleteEventView(LoginRequiredMixin,DeleteView):
    model=Event
    success_url =reverse_lazy('list_events_view')
    