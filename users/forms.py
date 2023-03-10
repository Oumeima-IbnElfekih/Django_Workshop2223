from django import forms
from users.models import Person
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class LoginForm(forms.ModelForm):
    class Meta:
        model=Person
        fields=['username','password']
    password =forms.CharField(label="Password",widget=forms.PasswordInput())
    

class RegisterForm(UserCreationForm):
    class Meta:
        model= get_user_model()
        fields=['cin','username','email','first_name',
                'last_name','password1','password2']
    def save(self, commit=True):
        return super(RegisterForm,self).save(commit)