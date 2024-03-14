from django.db import models
from django.contrib.auth.models import User

class Services(models.Model):
    service_icon = models.CharField(max_length=50)
    service_title = models.CharField(max_length=50)
    service_des=models.TextField()





