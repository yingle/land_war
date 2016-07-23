from django.db import models
from django.contrib.auth.models import User
# Create your models here.

KIND_CHOICES = (('BEACH', 'Beach'),('MOUNTAIN', 'Mountain'),('CASTEL', 'Castel'))


class Photo(models.Model):
    filename = models.CharField(max_length=100)
    kind = models.CharField(choices=KIND_CHOICES, max_length=50)
    upload_data = models.DateTimeField('date of upload')
    description = models.CharField(max_length=300)
    match_number = models.IntegerField(default=0)
    votes = models.IntegerField(default=50)
    createUser = models.ForeignKey(User)
    city = models.CharField(max_length=30)
    image = models.ImageField(upload_to="dir_upload/")
    #ci sara' anche il campo ImageField

    def __unicode__(self):
        return self.city
