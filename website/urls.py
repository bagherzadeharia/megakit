from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('project/', project, name="project"),
    path('services/', services, name="services"),
    path('404/', error_404, name="404"),
    path('403/', error_403, name="403"),
]
