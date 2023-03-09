from django.urls import path
from .views import home, signin, signup, signout
 
urlpatterns = [
    path("",home, name="home"),
    path("home/signin",signin, name="signin"),
    path("home/signup",signup, name="signup"),
    path("home/signout",signout, name = 'signout'),
]