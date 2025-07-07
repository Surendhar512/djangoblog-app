from django.urls import path
from .views import blog_home, blog_detail

urlpatterns = [
        path('',blog_home, name='blog_home'),
        path('<slug:slug>/',blog_detail,name='blog_detail'),
]