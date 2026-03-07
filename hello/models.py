from django.db import models

# Create your models here.

class User(models.Model):
    Email_or_Phone =models.CharField(max_length=250)
    Password = models.CharField(max_length=250)
