
from django.contrib import admin
from django.urls import path, include
from firstapp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('token_send/', views.token_send, name='token_send'),
    # path('signup/', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.LogoutPage, name='logout'),
    path('services/', views.services, name='services'),
    path('generate-pdf/<int:service_id>/', views.generate_pdf, name='generate_pdf'),
    path('generate-excel/<int:service_id>/', views.generate_excel, name='generate_excel'),
    path('download-csv/<int:service_id>/', views.download_csv, name='download_csv'),
    path('form/', views.form, name='form'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('success/', views.success, name='success'),
    path('verify/<verification_token>/', views.verify, name='verify'),
    path('error/', views.error_page, name='error'),
    path('approvalrequest/', views.ApprovalRequest, name='approvalrequest'),
    path('adminApproval/', views.AdminApproval, name='adminApproval'),
    path('send_acceptance_email/', views.send_acceptance_email, name='send_acceptance_email'),
    path('send_rejection_email/', views.send_rejection_email, name='send_rejection_email'),
    path('userdetails/',views.UserDetails,name='userdetails'),
    path('upload_profile_image/',views.upload_profile_image, name='upload_profile_image'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('display_services/',views.display_services,name='display_services'),
    path('navbar/',views.navbar,name='navbar'),
    # path('display_profile_picture/', views.display_profile_picture, name='display_profile_picture'),
]

    




