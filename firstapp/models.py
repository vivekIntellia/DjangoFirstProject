from django.db import models
from django.contrib.auth.models import AbstractUser

class firstapp(models.Model):
    firstapp_icon = models.CharField(max_length=50)
    firstapp_title = models.CharField(max_length=50)
    firstapp_des = models.TextField()



# Create your models here.

# Create your models here.
