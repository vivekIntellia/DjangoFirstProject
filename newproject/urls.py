"""
URL configuration for newproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from firstapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.SignupPage, name='signup'),
    path('signup/', views.SignupPage, name='signup'),
    path('userdetails/', views.UserDetails, name='userdetails'),
    path('approvalrequest/', views.ApprovalRequest, name='approvalrequest'),
    path('adminApproval/', views.AdminApproval, name='adminApproval'),
    path('send_acceptance_email/', views.send_acceptance_email, name='send_acceptance_email'),
    path('send_rejection_email/', views.send_rejection_email, name='send_rejection_email'),
    path('login/', views.LoginPage , name='login'),
    path('home/', views.HomePage , name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('services/', views.services , name='services'),
    path('generate-pdf/<int:service_id>/', views.generate_pdf, name='generate_pdf'),
    path('generate-excel/<int:service_id>/', views.generate_excel, name='generate_excel'),
    path('download-csv/<int:service_id>/', views.download_csv, name='download_csv'),
    path('form', views.form , name='form'),
    path('thankyou/', views.thankyou , name='thankyou'),
    # path('upload/', views.upload_image, name='upload_image'),
    # path('calculator/', views.calculator),

    # path('UserForms/', views.UserForms),
]
 
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


