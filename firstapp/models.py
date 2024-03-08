from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=100, blank=True, null=True)
    cerated_at=models.DateField(auto_now_add=True)


    def __str__(self):
        return self.user.username




