from .views import *
from django.urls import path
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/',signIn , name="login"),
    path('logout/',LogoutView.as_view(), name="logout")
]
