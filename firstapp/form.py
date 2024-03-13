# forms.py
from django import forms
from .models import Profile_picture

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile_picture
        fields = ['profile_picture']

