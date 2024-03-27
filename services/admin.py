from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Services

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id' , 'service_icon', 'service_title', 'service_des')

admin.site.register(Services, ServiceAdmin)

# Register CustomUser with UserAdmin

