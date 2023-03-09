from django import forms
from .models import User
#creating forms
class loginForm(forms.ModelForm):
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
            'password_repeat': forms.PasswordInput(),

        }
        fields = "__all__"
    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        password = cleaned_data.get("password")
        password_repeat = cleaned_data.get("password_repeat")

        if password != password_repeat:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )