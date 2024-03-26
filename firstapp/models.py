from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from viewflow import jsonstore
from viewflow.workflow.models import Process


# class User(AbstractUser):
#    gender = models.BooleanField(default=True)
class SignUp(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length = 50 , default=False)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.status = 'Pending'
        super().save(*args, **kwargs) 

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
    
class Profile_picture(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # profile_picture = models.ImageField(upload_to='profile_pics/', default='default_profile_picture.jpg')
    profile_picture = models.ImageField(upload_to='profile_pics/')

    def __str__(self):
        return self.user.username
    


class UserResponse(models.Model):
    response_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class_10_school_name = models.CharField(max_length=100, null=True, blank=True)
    class_10_board_or_university = models.CharField(max_length=100, null=True, blank=True)
    class_10_year_of_passing = models.IntegerField(null=True, blank=True)
    class_10_grade_or_cgpa = models.FloatField(null=True, blank=True)
    class_10_marksheet = models.ImageField(upload_to='marksheet/', null=True, blank=True)
    class_10_percentage = models.FloatField(null=True, blank=True)

    class_12_school_name = models.CharField(max_length=100, null=True, blank=True)
    class_12_board_or_university = models.CharField(max_length=100, null=True, blank=True)
    class_12_year_of_passing = models.IntegerField(null=True, blank=True)
    class_12_grade_or_cgpa = models.FloatField(null=True, blank=True)
    class_12_marksheet = models.ImageField(upload_to='marksheet/', null=True, blank=True)
    class_12_percentage = models.FloatField(null=True, blank=True)

    graduation_college_name = models.CharField(max_length=100, null=True, blank=True)
    graduation_board_or_university = models.CharField(max_length=100, null=True, blank=True)
    graduation_year_of_passing = models.IntegerField(null=True, blank=True)
    graduation_grade_or_cgpa = models.FloatField(null=True, blank=True)
    graduation_marksheet = models.ImageField(upload_to='marksheet/', null=True, blank=True)
    graduation_percentage = models.FloatField(null=True, blank=True)

    approved = models.BooleanField(default=False)  

    def __str__(self):
        return f"{self.user.username}'s Education Details"


