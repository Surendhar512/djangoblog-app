from django.urls import path
from .views import blog_home, blog_detail, create_post

urlpatterns = [
        path('',blog_home, name='blog_home'),
        path('new/',create_post,name='create_post'),
        path('<slug:slug>/',blog_detail,name='blog_detail'),
]