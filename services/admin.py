from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Services

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_icon', 'service_title', 'service_des')

admin.site.register(Services, ServiceAdmin)

# Register CustomUser with UserAdmin
# admin.site.register(Profile)
