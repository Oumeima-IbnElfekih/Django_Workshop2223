from .views import *
from django.urls import path

urlpatterns = [
     path('eventslist/', ListEvent ,name="list_events"),
     path('eventslistView/' , ListEventView.as_view(),name='list_events_view') 
]
