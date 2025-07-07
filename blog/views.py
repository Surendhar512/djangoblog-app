from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import BlogPost

# Create your views here.

def blog_home(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})  

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog/detail.html', {'post': post})
