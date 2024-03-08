from django.db import models
from django.contrib.auth.models import User

class Services(models.Model):
    service_icon = models.CharField(max_length=50)
    service_title = models.CharField(max_length=50)
    service_des=models.TextField()

# class Profile(models.Model):
#     user = models.OneToOneField(User , on_delete = models.CASCADE , related_name = 'Profile')
#     image = models.ImageField(upload_to = 'pics')



