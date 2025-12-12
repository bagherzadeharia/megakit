from pathlib import Path
from megakit.settings import *
from megakit.settings import BASE_DIR

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR inherited from main settings.py

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-z!smqw*tytx^tbvar4a++a-(02c+((es7-5@9qhzlm7c3c9uc$"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# INSTALLED_APPS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

STATIC_ROOT = BASE_DIR / "static_root"
MEDIA_ROOT = BASE_DIR / "media"

STATICFILES_DIRS = [BASE_DIR / "static"]

# Related to 'debug_toolbar'
# INTERNAL_IPS = ["127.0.0.1", "localhost", "0.0.0.0"]

X_FRAME_OPTIONS = "SAMEORIGIN"
