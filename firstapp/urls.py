# Comment out or remove the lines you don't need
# path('home/' , include(views.about) , name='about'),
# path('', include(views.SignupPage) , name="Signuppage"),
# path('login/', include(views.LoginPage) , name="LoginPage"),
# path('logout/', include(views.LogoutPage) , name='logout'),
# path('services' , include(views.services) , name='services'),
# path('' , include(views.form) , name='form'),
# path('thankyou' , include(views.thankyou) , name='thankyou'),
# path('verify/<str:token>/',views.verify_email, name='verify_email'),

# Remove the extra ']' at the end
# ]

# Correct urlpatterns
from django.contrib import admin
from django.urls import path, include
from firstapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.LogoutPage, name='logout'),
    path('services/', views.services, name='services'),
    path('generate-pdf/<int:service_id>/', views.generate_pdf, name='generate_pdf'),
    path('generate-excel/<int:service_id>/', views.generate_excel, name='generate_excel'),
    path('download-csv/<int:service_id>/', views.download_csv, name='download_csv'),
    path('form/', views.form, name='form'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('token_send/', views.token_send, name='token_send'),
    path('success/', views.success, name='success'),
    path('verify/<verification_token>', views.verify, name='verify'),
    path('error/', views.error_page, name='error'),

    # Include other paths as needed

    # path('upload/', views.upload_image, name='upload_image'),
    # path('calculator/', views.calculator),

    # path('UserForms/', views.UserForms),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
