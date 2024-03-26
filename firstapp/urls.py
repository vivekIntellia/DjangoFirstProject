
from django.contrib import admin
from django.urls import path, include


from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import patterns , include , url

from django.contrib.auth import views as auth_views
from . forms import MyPasswordchangeField,MyPasswordResetForm,MySetPasswordForm
from viewflow.contrib.auth import AuthViewset
from viewflow.urls import Application, Site, ModelViewset
from viewflow.workflow.flow import FlowAppViewset
# from viewflow.workflow import viewsite
# from .views import SignUpStartView
from .flows import SignupFlow 
from .views import SignupPage
from firstapp import views
from viewflow import views as vf_views

site = Site(title="ACME Corp", viewsets=[
    Application(
        title='Signup', icon='people', app_name='firstapp', viewsets=[
            FlowAppViewset(SignupFlow , icon="assignment"),
        ]
    ),
])

from .views import education_form_view, MakeDecisionView


urlpatterns = [
    # path('flows/', include('viewsite.urls')),
    # path('admin/', admin.site.urls),
    path('accounts/', AuthViewset(with_profile_view=False).urls),
    path('', site.urls),
    # path('workflow/', site.urls),
    # path("workflow/", include("viewflow.urls")),
    # path("signup/start/", SignupPage.as_view(), name="signup_start"),
    path('token_send/', views.token_send, name='token_send'),
    path('signup/', views.SignupPage, name='signup'),
    path('CompleteProfile/', views.CompleteProfile, name='CompleteProfile'),
    path('profileApproval/', views.profileApproval, name='profileApproval'),
    path('profileRejected/', views.profileRejected, name='profileRejected'),
    path('', views.SignupPage, name='signup'),
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
    path('send_profile_acceptance_email/<int:signup_obj_id>/', views.send_profile_acceptance_email, name='send_profile_acceptance_email'),
    path('send_profile_rejection_email/<int:signup_obj_id>/', views.send_profile_rejection_email, name='send_profile_rejection_email'),
    path('rejected/',views.rejected,name='rejected'),
    path('userdetails/',views.UserDetails,name='userdetails'),
    path('upload_profile_image/',views.upload_profile_image, name='upload_profile_image'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('display_services/',views.display_services,name='display_services'),
    path('chatbot/save_response', views.save_response, name='save_response'),
    path('chatbot/',views.chatbot,name='chatbot'),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='passwordchange.html', form_class=MyPasswordchangeField, success_url='/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name='passwordchangedone.html'),name='passwordchangedone'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password-reset_confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('password-reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    path('fill_education/',education_form_view, name='fill_education'), 
    path('admin_notification/',views.admin_notification,name='admin_notification'),
    path('make_decision/<int:education_id>/', MakeDecisionView.as_view(), name='make_decision'),
    # path('workflow/', include('viewflow.urls')),
    # path('display_profile_picture/', views.display_profile_picture, name='display_profile_picture'),

# urlpatterns = patterns(
#     '',
#     url(r'^flows/' , include(viewsite.urls)),
#     url(r'^admin/' , include(admin.site.urls))
# )
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    




