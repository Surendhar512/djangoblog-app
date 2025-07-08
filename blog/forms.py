# blog/forms.py

from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control my-title-field', 
                'placeholder': 'Enter blog title...'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control url-slug', 
                'placeholder': 'auto-generated-from-title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control blog-editor', 
                'rows': 6,
                'placeholder': 'Write your blog content here...'
            }),
        }
