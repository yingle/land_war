from django import forms
from django.contrib import admin


class RegistrationForm(forms.Form):
    Username = forms.CharField(max_length=30)
    FirstName = forms.CharField(max_length=30)
    LastName = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Password = forms.CharField(max_length=30)
