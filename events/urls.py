from .views import *
from django.urls import path

urlpatterns = [
     path('eventslist/', ListEvent ,name="list_events"),
     path('addevent/', add_event ,name="add_event"),
     path('createevent/', create_event ,name="create_event"),
     path('participate/<int:event_id>', participate,name="participate"),
     path('eventslistView/' , ListEventView.as_view(),name='list_events_view') ,
     path('eventsCreateView/' , CreateEvent.as_view(),name='create_events_view') ,
     path('eventsUpdateView/<int:pk>' , UpdateEvent.as_view(),name='update_events_view') ,
     path('eventDetails/<int:pk>',DetailEventView.as_view(),name='event_details'),
     path('eventsDeleteView/<int:pk>',DeleteEventView.as_view(),name="delete_event_view")
]
