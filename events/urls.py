from .views import *
from django.urls import path

urlpatterns = [
     path('eventslist/', ListEvent ,name="list_events"),
     path('addevent/', add_event ,name="add_event"),
     path('eventslistView/' , ListEventView.as_view(),name='list_events_view') ,
     path('eventDetails/<int:pk>',DetailEventView.as_view(),name='event_details')
]
