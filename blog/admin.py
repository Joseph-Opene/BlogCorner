#this is where we register our models to show in the admin page
from django.contrib import admin
from .models import Post, Likes, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Likes)
admin.site.register(Comment)
