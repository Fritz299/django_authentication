from django.shortcuts import render, redirect
from .forms import loginForm,UserRegistrationForm
from . import models
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import forms
 
 # Create your views here.

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('home/signin')
    

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signup.html',{'form':form})
        
    else:
        form = UserRegistrationForm()
        return render(request,'signup,html',{'form':form})
    

def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = loginForm(request.POST)
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username,password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            form = loginForm()
            return render(request, 'signin.html',{'form':form})
    else:
        form = loginForm()
        return render(request, 'signin.html',{'form':form})
    

def signout(request):
    logout(request)
    return redirect('home/signin/')
