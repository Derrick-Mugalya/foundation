from django.db import models
from django.contrib.auth.models import User
import datetime
from datetime import date
from django.utils import timezone

# Create your models here.

class Entryform(models.Model):
    owner = models.ForeignKey(User, related_name='Entryform', on_delete=models.CASCADE)
    code = models.IntegerField(default=0)
    dob = models.DateField(blank=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    whyassist = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    religion = models.CharField(max_length=100)
    fathersname = models.CharField(max_length=100)
    fathersoccupation = models.CharField(max_length=100)
    mothersname = models.CharField(max_length=100)
    mothersoccupation = models.CharField(max_length=100)
    brothers = models.CharField(max_length=100)
    sisters = models.CharField(max_length=100)
    guardian = models.CharField(max_length=100)
    guardiansoccupation = models.CharField(max_length=100)
    homelocation = models.CharField(max_length=100)
    hometype = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    favorites = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='static/images', default='https://th.bing.com/th/id/R.1a169ee0e11d6f85260b7864aa916f2c?rik=F6uhG3K5RxD0Bg&pid=ImgRaw&r=0')
    datecommence = models.DateField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.firstname}'
    class Meta:
        verbose_name_plural = 'EntryForm'