from django.contrib import admin
from .models import BlogPost
# Register your models here.

# admin.site.register(BlogPost, BlogPostAdmin)
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'created_at')
    ordering = ('-created_at',)