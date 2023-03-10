from django.shortcuts import render
from .forms import LoginForm ,RegisterForm
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
    
    
    
def signUp(req):
    form =RegisterForm()
    if req.method=="POST":
        form=RegisterForm(req.POST)
        print(req.POST)
        if form.is_valid():
            user=form.save()
            login(req,user=user)
            return redirect('list_events_view')
    return render(req,"users/form.html",{"form":form})