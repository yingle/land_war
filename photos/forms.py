from django import forms
from django.db import models
from django.forms import ModelForm
from models import *

KIND_CHOICES = (('BEACH', 'Beach'),('MOUNTAIN', 'Mountain'),('CASTEL', 'Castel'))


class UploadImageForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'kind','city', 'description' ]
    image = forms.ImageField()
    kind = forms.ChoiceField(choices=KIND_CHOICES)
    city = forms.CharField(max_length=30)
    description = forms.CharField(widget=forms.Textarea, max_length=300)