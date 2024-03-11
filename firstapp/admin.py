from django.contrib import admin

from firstapp.models import *

class firstappAdmin(admin.ModelAdmin):
        list_display = ('firstapp_icon' , 'firstapp_title' , 'firstapp_des')



admin.site.register(UserProfile)

