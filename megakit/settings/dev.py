from pathlib import Path
from megakit.settings import *
from megakit.settings import BASE_DIR
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR inherited from main settings.py

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

ALLOWED_HOSTS = ['*']

# Sites Framework
SITE_ID = 1

STATIC_ROOT = BASE_DIR / "static_root"
MEDIA_ROOT = BASE_DIR / "media"

# Related to 'debug_toolbar'
# INTERNAL_IPS = ["localhost", "127.0.0.1", "0.0.0.0"]

X_FRAME_OPTIONS = "SAMEORIGIN"

# Email backend for development - prints emails to console

EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

X_FRAME_OPTIONS = "SAMEORIGIN"
