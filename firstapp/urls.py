from django.contrib import admin
from django.urls import path , include
from firstapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/' , include(views.HomePage) , name='about'),
    path('', include(views.SignupPage) , name="Signuppage"),
    path('userdetails/', include(views.UserDetails) , name="UserDetails"),
    # path('approvalrequest/', include(views.ApprovalRequest) , name="ApprovalRequest"),
    path('login/', include(views.LoginPage) , name = "LoginPage"),
    path('logout/', include(views.LogoutPage) , name='logout'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('services' , include(views.services) , name='services'),
    path('' , include(views.form) , name='form'),
    path('thankyou' , include(views.thankyou) , name='thankyou'),
    # path('calculator' , include(views.calculator) , name='calculator'),

    # path('UserForms' , include(views.UserForms) , name='UserForms'),


]

