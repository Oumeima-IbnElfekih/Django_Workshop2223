from .views import *
from django.urls import path

urlpatterns = [
     path('eventslist/', ListEvent ,name="list_events")
]
