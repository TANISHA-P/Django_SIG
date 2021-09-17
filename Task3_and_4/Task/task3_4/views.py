from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import *



def index(request):
    if not(request.user.is_authenticated):
        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "index.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html",{
                "message": "Invalid credentials"
            })
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return render(request,"login.html",{
        "message":"Succesfully Logged Out."
    })

def registration_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            return render(request, "login.html",{
                'message': "Registration succesfull !! Login to continue"
            })
        return render(request,"register.html",{
            'message':"Error. Register again",
            'form': form
        })
    else:
        form = RegistrationForm()
        return render(request,"register.html",{
            'form': form
        })
   