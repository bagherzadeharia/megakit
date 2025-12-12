from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "website/index.html")

def about(request):
    return render(request, "website/about.html")

def contact(request):
    return render(request, "website/contact.html")

def project(request):
    return render(request, "website/project.html")

def services(request):
    return render(request, "website/service.html")

def error_404(request):
    return render(request, "website/error-404.html")

def error_403(request):
    return render(request, "website/error-403.html")
