"""
URL configuration for megakit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from blog.sitemaps import BlogSitemap
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import BlogSitemap
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap
import django.contrib.auth.urls
# import debug_toolbar
import django_summernote
from website.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('blog/', include('blog.urls')),
    # path('__debug__/', include('debug_toolbar.urls', namespace='djdt')),
    path('captcha/', include('captcha.urls')), # Captcha
    path('accounts_app/', include('accounts.urls')), # The 'accounts' application
    path('accounts/', include('django.contrib.auth.urls')),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"), # The 'sitemaps' framework
    path("robots.txt", include('robots.urls')), # The 'robots' framework
    path("summernote/", include('django_summernote.urls')) # The 'summernote' module
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)