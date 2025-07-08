from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.

def blog_home(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})  

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog/detail.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_home')
        
    else:
        form = BlogPostForm()

    return render(request, 'blog/new_post.html', {'form': form})