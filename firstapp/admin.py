from django.contrib import admin
from firstapp.models import firstapp

class firstappAdmin(admin.ModelAdmin):
        list_display = ('firstapp_icon' , 'firstapp_title' , 'firstapp_des')

admin.site.register(firstapp, firstappAdmin)
# Register your models here.


# Register your models here.
