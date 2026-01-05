from pathlib import Path
from megakit.settings import *
from megakit.settings import BASE_DIR
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR inherited from main settings.py

# Quick-start production settings - unsuitable for development
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = ['*']

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': config('DATABASE_PROD_ENGINE', default='django.db.backends.postgresql'),
        'NAME': config('DATABASE_PROD_NAME', default='megakit_db'),
        'USER': config('DATABASE_PROD_USER'),
        'PASSWORD': config('DATABASE_PROD_PASSWORD'),
        'HOST': config('DATABASE_PROD_HOST'),
        'PORT': config('DATABASE_PROD_PORT', default=5432, cast=int),
    }
}

# Sites Framework
SITE_ID = 1

STATIC_ROOT = '/usr/src/app/staticfiles'
MEDIA_ROOT = '/usr/src/app/media'

CSRF_COOKIE_SECURE = True

STATICFILES_DIRS = []

# Related to 'debug_toolbar'
# INTERNAL_IPS = ["localhost", "127.0.0.1", "0.0.0.0"]

EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

X_FRAME_OPTIONS = "SAMEORIGIN"
