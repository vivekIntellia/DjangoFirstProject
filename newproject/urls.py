from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('accounts/', AuthViewset(with_profile_view=False).urls),
    path('admin/', admin.site.urls),
    # path('', views.SignupPage, name='signup'),
    path('', include('firstapp.urls')), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
