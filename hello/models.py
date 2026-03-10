from django.db import models

# Create your models here.

class User(models.Model):
    Username =models.CharField(max_length=250)
    Email =models.EmailField(unique=True,null=True, blank=True)
    Phone_Number = models.CharField(max_length=20,null=True,blank=True)
    Password = models.CharField(max_length=250)

    def __str__(self):
        return self.Username
    
class EmailOTP(models.Model):
        email = models.EmailField()
        otp = models.CharField(max_length=6)

        def __str__(self):
            return self.email
            