from django.db import models
from django.contrib import auth
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Admin(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return self.username


class Trainer(models.Model):
    name = models.CharField(max_length=55)
    username = models.CharField(max_length=55)
    email = models.EmailField()
    password = models.CharField(max_length=55)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse( "trainer:trainerDetail",kwargs={'pk':self.pk} )


class Member(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    age = models.IntegerField(max_length=255)
    height = models.FloatField(max_length=255)
    weight = models.FloatField(max_length=255)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse( "manager:memberDetail",kwargs={'pk':self.pk} )


class Fee(models.Model):
    member = models.ForeignKey(
        Member, related_name='fee', on_delete=models.CASCADE)
    amount = models.IntegerField(max_length=255)
    month = models.CharField(max_length=255)
    date_paid = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.month

    def get_absolute_url(self):
        return reverse( "manager:adminDash" )

    
