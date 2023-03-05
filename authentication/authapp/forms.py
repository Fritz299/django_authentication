
from django import forms
from .models import User
#creating forms
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username',
                  'password'
                 ]
class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = "__all__"