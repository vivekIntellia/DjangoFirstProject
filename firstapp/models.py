from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from .manager import UserManager
<<<<<<< Updated upstream

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone
=======
>>>>>>> Stashed changes




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=100, blank=True, null=True)
    cerated_at=models.DateField(auto_now_add=True)


    def __str__(self):
        return self.user.username
    

# class PhoneOTP(AbstractUser):
#     phone_number = models.CharField(max_length=15, unique=True)
#     otp = models.CharField(max_length=6)
#     is_verified = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)

#     USERNAME_FIELD = 'phone_number'
#     REQUIRED_FIELDS = []
#     objects = UserManager()

#     def __str__(self):
#         return f"{self.username} - {self.phone_number}"

#     # Provide unique related_names for the conflicting relationships
#     groups = models.ManyToManyField('auth.Group', related_name='phoneotp_groups', blank=True)
#     user_permissions = models.ManyToManyField('auth.Permission', related_name='phoneotp_user_permissions', blank=True)

#     class Meta:
#         # You can keep this if needed
#         unique_together = ('phone_number', 'username')
    

# models.py
# models.py

<<<<<<< Updated upstream
=======
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone
>>>>>>> Stashed changes

class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The Phone number field must be set')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone_number, password, **extra_fields)

class PhoneOTP(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=15, unique=True)
    otp = models.CharField(max_length=6)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.phone_number}"

    # Provide unique related_names for the conflicting relationships
    groups = models.ManyToManyField('auth.Group', related_name='phoneotp_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='phoneotp_user_permissions', blank=True)


<<<<<<< Updated upstream

    
=======
>>>>>>> Stashed changes








class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sport = models.CharField(max_length=100)
    school_experience = models.CharField(max_length=100)
    state_experience = models.CharField(max_length=100)
    national_experience = models.CharField(max_length=100)
    international_experience = models.CharField(max_length=100)

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
