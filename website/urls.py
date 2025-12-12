from django.contrib import admin
from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('project/', project, name="project"),
    path('services/', services, name="services"),
    path('error-404/', error_404, name="error_404"),
    path('error-403/', error_403, name="error_403"),
]
