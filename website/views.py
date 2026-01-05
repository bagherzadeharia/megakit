from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from website.forms import ContactForm

def index(request):
    return render(request, "website/index.html")

def about(request):
    return render(request, "website/about.html")

def contact(request):
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Your message has been sent successfully.'})
            else:
                messages.success(request, "Your message has been sent successfully.")
                return redirect('website:contact')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'message': 'There was an error in your form. Please check the fields.', 'errors': form.errors})
            else:
                messages.error(request, "There was an error in your form. Please check the fields.")
    else:
        form = ContactForm()

    return render(request, "website/contact.html", {'form': form})

def project(request):
    return render(request, "website/project.html")

def services(request):
    return render(request, "website/service.html")

def error_404(request):
    return render(request, "404.html", status=404)

def error_403(request):
    return render(request, "403.html", status=403)
