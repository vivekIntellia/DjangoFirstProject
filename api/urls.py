from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('viewlist/',views.ViewList.as_view(), name='post_list'),
    path('addpost/',views.AddPost.as_view(),name='Add_List'),
    # path('details/<str:pk>',views.PostDetails.as_view(), name='post_details'),
    # path('api/',views.my_template_view,name='api'),
    path('apii/',views.postt,name='post'),
    path('posts/<int:pk>/', views.PostDetails.as_view()),
    path('posts/<int:post_id>/comments/', views.CommentList.as_view()),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)