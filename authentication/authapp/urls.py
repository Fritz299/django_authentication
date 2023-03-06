from django.urls import path, include
from django.contrib import admin
from . import views
from .forms import UserRegistrationForm, loginForm
 
urlpatterns = [
    path("",views.home,),
    path("home/signin",views.signin, ),
    path("/home/signup",views.signup),
    path("home/signout",views.signout, name = 'logout'),
]