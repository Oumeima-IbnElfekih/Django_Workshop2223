from django import forms
from users.models import Person




class LoginForm(forms.ModelForm):
    class Meta:
        model=Person
        fields=['username','password']
    password =forms.CharField(label="Password",widget=forms.PasswordInput())
    