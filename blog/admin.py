from django.shortcuts import render
from django.contrib import admin
from .models import Post

admin.site.register(Post)