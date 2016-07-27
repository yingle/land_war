from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone
from datetime import *

# Create your models here.

KIND_CHOICES = (('BEACH', 'Beach'),('MOUNTAIN', 'Mountain'),('CASTEL', 'Castel'))


class Photo(models.Model):
    #filename = models.CharField(max_length=100)
    kind = models.CharField(choices=KIND_CHOICES, max_length=50)
    upload_date = models.DateTimeField('date of upload')
    description = models.CharField(max_length=300)
    match_number = models.IntegerField(default=0)
    votes = models.FloatField(default=50.00)
    createUser = models.ForeignKey(User)
    city = models.CharField(max_length=30)
    image = models.ImageField(upload_to='dir_upload')
    #ci sara' anche il campo ImageField

    def __unicode__(self):
        return self.kind+' [ '+self.city+' ] '

    def was_uploaded_recently(self):
        return self.upload_date >= timezone.now()- datetime.timedelta(days=1)

    was_uploaded_recently.admin_order_field = 'upload_date'
    was_uploaded_recently.boolean = True
    was_uploaded_recently.short_description = 'Uploaded recently?'


class DailyWinner(models.Model):
    race_date = models.DateField()
    #relazione manyToOne
    winnerPhoto = models.ForeignKey(Photo, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.race_date