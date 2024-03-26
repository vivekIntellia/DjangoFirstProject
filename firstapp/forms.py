from django import forms
from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from .models import Education




class MyPasswordchangeField(PasswordChangeForm):
    old_password=forms.CharField(label=("Old Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}))
    new_password1=forms.CharField(label=("New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2=forms.CharField(label=("Confirm New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))
    
class MyPasswordResetForm(PasswordResetForm): 
    email = forms.EmailField(label=("Email"),max_length=254, widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1=forms.CharField(label=("New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2=forms.CharField(label=("Confirm New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))
 


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = [
            'class_10_school_name', 'class_10_board_or_university', 'class_10_year_of_passing', 'class_10_grade_or_cgpa',
            'class_10_marksheet', 'class_10_percentage',
            'class_12_school_name', 'class_12_board_or_university', 'class_12_year_of_passing', 'class_12_grade_or_cgpa',
            'class_12_marksheet', 'class_12_percentage',
            'graduation_college_name', 'graduation_board_or_university', 'graduation_year_of_passing', 'graduation_grade_or_cgpa',
            'graduation_marksheet', 'graduation_percentage',
        ]



        
    def clean(self):
        cleaned_data = super().clean()

        # Validate Class 10 CGPA
        class_10_cgpa = cleaned_data.get('class_10_grade_or_cgpa')
        if class_10_cgpa is not None and class_10_cgpa > 10:
            raise ValidationError({'class_10_grade_or_cgpa': 'CGPA should not be greater than 10.'})

        class_10_percentage = cleaned_data.get('class_10_percentage')
        if class_10_percentage is not None and class_10_percentage > 100:
            raise ValidationError({'class_10_percentage': 'Percentage should not be greater than 100.'})
        
        class_10_year_of_passing = cleaned_data.get('class_10_year_of_passing')
        if class_10_year_of_passing is not None and len(str(class_10_year_of_passing)) != 4:
            raise ValidationError({'class_10_year_of_passing': 'Please enter a valid year.'})
        

        #12th class validation details


        class_12_cgpa = cleaned_data.get('class_12_grade_or_cgpa')
        if class_12_cgpa is not None and class_12_cgpa > 10:
            raise ValidationError({'class_12_grade_or_cgpa': 'CGPA should not be greater than 10.'})

        class_12_percentage = cleaned_data.get('class_12_percentage')
        if class_12_percentage is not None and class_12_percentage > 100:
            raise ValidationError({'class_12_percentage': 'Percentage should not be greater than 100.'})

        class_12_year_of_passing = cleaned_data.get('class_12_year_of_passing')
        if class_12_year_of_passing is not None and len(str(class_12_year_of_passing)) != 4:
            raise ValidationError({'class_12_year_of_passing': 'Please enter a valid year.'})
        

#    graduation validation code 
        graduation_grade_or_cgpa = cleaned_data.get('graduation_grade_or_cgpa')
        if graduation_grade_or_cgpa is not None and graduation_grade_or_cgpa > 10:
            raise ValidationError({'graduation_grade_or_cgpa': 'CGPA should not be greater than 10.'})

        graduation_percentage = cleaned_data.get('graduation_percentage')
        if graduation_percentage is not None and graduation_percentage > 100:
            raise ValidationError({'graduation_percentage': 'Percentage should not be greater than 100.'})

        graduation_year_of_passing = cleaned_data.get('graduation_year_of_passing')
        if graduation_year_of_passing is not None and len(str(graduation_year_of_passing)) != 4:
            raise ValidationError({'graduation_year_of_passing': 'Please enter a valid year.'})




        return cleaned_data


class ReviewEducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = [
            'class_10_school_name', 'class_10_board_or_university', 'class_10_year_of_passing', 'class_10_grade_or_cgpa',
            'class_12_school_name', 'class_12_board_or_university', 'class_12_year_of_passing', 'class_12_grade_or_cgpa',
            'graduation_college_name', 'graduation_board_or_university', 'graduation_year_of_passing', 'graduation_grade_or_cgpa',
        ]




