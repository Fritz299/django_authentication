from django.shortcuts import render, redirect
from .forms import UserForm
from . import models
from django.http import HttpResponse
 
 # Create your views here.
def UserRegistrationForm(request):
    print(request.POST)
    return render(request,'RegistrationForm.html')
 



