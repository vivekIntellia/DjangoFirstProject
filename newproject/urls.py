from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from firstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.SignupPage, name='signup'),
    path('', include('firstapp.urls')),  # Include the app's URLs
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
