from django.urls import path
from .views import UserRegistrationForm
 
urlpatterns = [
    path('', UserRegistrationForm),
]