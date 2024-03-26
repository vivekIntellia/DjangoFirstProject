from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from firstapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.SignupPage, name='signup'),
    path('', include('firstapp.urls')),  
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from firstapp import views

# from django.urls import path
# from viewflow.flow.viewset import FlowViewSet
# from firstapp.flows import EducationFlow

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('signup/', views.SignupPage, name='signup'),  # Changed URL to avoid conflict
#     path('firstapp/', include('firstapp.urls')),  # Changed URL to avoid conflict
#      path('education_flow/', FlowViewSet(EducationFlow).urls, name='start_education_flow'),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

