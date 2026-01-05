from django.contrib import admin
from django.urls import path
from blog.feeds import LatestEntriesFeed
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_home, name="blog_home"),
    path("search", blog_search, name="search"),
    path("tag/<str:tagName>", blog_home, name="tag"),
    path("post/<int:postID>", blog_single, name="single"),
    path("author/<str:authorUsername>", blog_home, name="author"),
    path("category/<slug:categoryName>", blog_home, name="category"),
    path("create_post", blog_new_post, name="create_post"),
    path("rss/feed/", LatestEntriesFeed())
]
