
from django.contrib import admin
from django.urls import path, include
from firstapp import views

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from . forms import MyPasswordchangeField,MyPasswordResetForm,MySetPasswordForm

urlpatterns = [
    path('token_send/', views.token_send, name='token_send'),
    path('signup/', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.LogoutPage, name='logout'),
    path('services/', views.services, name='services'),
    path('generate-pdf/<int:service_id>/', views.generate_pdf, name='generate_pdf'),
    path('generate-excel/<int:service_id>/', views.generate_excel, name='generate_excel'),
    path('download-csv/<int:service_id>/', views.download_csv, name='download_csv'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('success/', views.success, name='success'),
    path('verify/<verification_token>/', views.verify, name='verify'),
    path('error/', views.error_page, name='error'),
    path('approvalrequest/', views.ApprovalRequest, name='approvalrequest'),
    path('adminApproval/', views.adminApproval, name='adminApproval'),
    path('send_acceptance_email/<int:user_detail_id>/', views.send_acceptance_email, name='send_acceptance_email'),
    path('send_rejection_email/<int:user_detail_id>/', views.send_rejection_email, name='send_rejection_email'),
    path('rejected/',views.rejected,name='rejected'),
    path('userdetails/',views.UserDetails,name='userdetails'),
    path('upload_profile_image/',views.upload_profile_image, name='upload_profile_image'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('display_services/',views.display_services,name='display_services'),
    path('navbar/',views.navbar,name='navbar'),
    path('chatbot/save_response', views.save_response, name='save_response'),
    path('chatbot/',views.chatbot,name='chatbot'),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='passwordchange.html', form_class=MyPasswordchangeField, success_url='/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name='passwordchangedone.html'),name='passwordchangedone'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password-reset_confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('password-reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    
    # path('display_profile_picture/', views.display_profile_picture, name='display_profile_picture'),
]

    




