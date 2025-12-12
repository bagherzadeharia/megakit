from django.contrib import admin
from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_home, name="blog_home"),
    path("search", blog_search, name="search"),
    # path("tag/<str:tagName>", blog_home, name="tag"),
    path("post/<int:postID>", blog_single, name="single"),
    path("author/<str:authorUsername>", blog_home, name="author"),
    path("category/<str:categoryName>", blog_home, name="category"),
]
