from django.shortcuts import render
from .forms import LoginForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate ,login
# Create your views here.



def signIn(req):
    form = LoginForm()
    if req.method=="GET":
        return render(req,"users/form.html",{'form': form})
    if req.method =="POST":
        username= req.POST['username']
        pwd =req.POST['password']
        user = authenticate(req,username=username,password=pwd)
        if user is not None:
            login(request=req,user=user)
            return redirect('list_events_view')
        else :
            return render(req,"users/form.html",{ "error":"invalid credentials","form":form })
    