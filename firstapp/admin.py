from django.contrib import admin
from .models import UserProfile, UserDetail

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass
  
@admin.register(UserDetail)
class UserDetailAdmin(admin.ModelAdmin):
    list_display = ['user', 'sport', 'formatted_school_experience', 'formatted_state_experience', 'formatted_national_experience', 'formatted_international_experience']

    def formatted_school_experience(self, obj):
        return f"{obj.school_experience} Years"
    formatted_school_experience.short_description = 'School Experience'

    def formatted_state_experience(self, obj):
        return f"{obj.state_experience} Years"
    formatted_state_experience.short_description = 'State Experience'

    def formatted_national_experience(self, obj):
        return f"{obj.national_experience} Years"
    formatted_national_experience.short_description = 'National Experience'

    def formatted_international_experience(self, obj):
        return f"{obj.international_experience} Years"
    formatted_international_experience.short_description = 'International Experience'

