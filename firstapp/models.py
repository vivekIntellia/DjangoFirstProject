from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=100, blank=True, null=True)
    created_at=models.DateField(auto_now_add=True)


    def __str__(self):
        return self.user.username

class UserDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sport = models.CharField(max_length=100)
    school_experience = models.CharField(max_length=100)
    state_experience = models.CharField(max_length=100)
    national_experience = models.CharField(max_length=100)
    international_experience = models.CharField(max_length=100)
    status = models.CharField(max_length = 50)
    note = models.TextField()

    def get_sport_label(self):
        sport_labels = {
            "1": "Football",
            "2": "Table Tennis",
            "3": "Volleyball",
            "4": "Chess",
            "5": "Basketball",
            "6": "Skating"
        }
        return sport_labels.get(self.sport, "Unknown")
    
    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if not self.pk:
            self.status = 'Pending'
        super().save(*args, **kwargs) 
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.status = 'Pending'
        super().save(*args, **kwargs) 
    
# models.py
class Profile_picture(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default_profile_picture.jpg')

    def __str__(self):
        return self.user.username
    


class UserResponse(models.Model):
    response_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

