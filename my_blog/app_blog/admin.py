from django.contrib import admin
from app_blog.models import Post, PostCategory, Quote

admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Quote)
