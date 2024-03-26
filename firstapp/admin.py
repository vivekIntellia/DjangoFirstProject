from django.contrib import admin
from .models import UserProfile, UserDetail,Profile_picture,UserResponse,SignUp,Education
from django.contrib.auth.admin import UserAdmin 
from django.contrib.auth.models import User


class SignupInline(admin.StackedInline):
    model = SignUp
    can_delete = False
    verbose_name_plural = 'Signup'

class CustomizedUserAdmin(UserAdmin):
    inlines = (SignupInline,)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass
@admin.register(UserDetail)
class UserDetailAdmin(admin.ModelAdmin):
    list_display = ['user', 'sport', 'formatted_school_experience', 'formatted_state_experience', 'formatted_national_experience', 'formatted_international_experience' , 'formatted_status' , 'formatted_note']

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

    def formatted_status(self, obj):
        return f"{obj.status}"
    formatted_status.short_description = 'Status'

    def formatted_note(self, obj):
        return f"{obj.note}"
    formatted_note.short_description = 'Note'

@admin.register(SignUp)
class SignUpAdmin(admin.ModelAdmin):
    list_display = ['user', 'formatted_fname', 'formatted_lname', 'formatted_gender', 'formatted_phone', 'formatted_city', 'formatted_zip' , 'formatted_state' , 'formatted_country']

    def formatted_fname(self, obj):
        return f"{obj.fname}"
    formatted_fname.short_description = 'First Name'

    def formatted_lname(self, obj):
        return f"{obj.lname}"
    formatted_lname.short_description = 'Last Name'

    def formatted_gender(self, obj):
        return f"{obj.gender}"
    formatted_gender.short_description = 'Gender'

    def formatted_phone(self, obj):
        return f"{obj.phone}"
    formatted_phone.short_description = 'Phone'

    def formatted_city(self, obj):
        return f"{obj.city}"
    formatted_city.short_description = 'City'

    def formatted_state(self, obj):
        return f"{obj.state}"
    formatted_state.short_description = 'State'

    def formatted_country(self, obj):
        return f"{obj.country}"
    formatted_country.short_description = 'Country'

    def formatted_zip(self, obj):
        return f"{obj.zip_code}"
    formatted_zip.short_description = 'Zip'


admin.site.register(Profile_picture)
admin.site.register(UserResponse)
admin.site.register(Education)
admin.site.unregister(User)
admin.site.register(User , CustomizedUserAdmin)



