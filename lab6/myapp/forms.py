from django import forms
from .models import *


class RegistrationForm(forms.Form):
    username = forms.CharField(min_length=4, label='Логин')
    password = forms.CharField(min_length=3, widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(min_length=3, widget=forms.PasswordInput, label='Повторите пароль')
