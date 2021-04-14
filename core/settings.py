"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 2.2.17.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "secret")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get("DEBUG"))

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_results',
    'django_celery_beat',
    'django_filters',
    'rest_framework',
    'drf_spectacular',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "django.middleware.locale.LocaleMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASE_URL = os.environ.get('DATABASE_URL', "sqlite:///db.sqlite")

DATABASES = {}

DATABASES['default'] = dj_database_url.config(conn_max_age=600)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        'LOCATION': 'cache:11211',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = os.environ.get("LANGUAGE_CODE", "de-ch")

TIME_ZONE = os.environ.get("TIME_ZONE", "Europe/Zurich")

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = '/media'
STATIC_ROOT = '/static'

LOCALE_PATHS = ['locale/']

# Celery

CELERY_BROKER_URL = "redis://redis:6379"

CELERY_RESULT_BACKEND = "django-db"

CELERY_CACHE_BACKEND = "django-cache"

CELERY_TIMEZONE = TIME_ZONE

# E-Mail

DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL",
                                    "webmaster@localhost")
SERVER_EMAIL = os.environ.get("SERVER_EMAIL", "root@localhost")

EMAIL_HOST = os.environ.get("SMTP_HOST", "smtp")
EMAIL_PORT = int(os.environ.get("SMTP_PORT", "25"))

EMAIL_USE_TLS = int(os.environ.get("SMTP_TLS", "0"))
EMAIL_USE_SSL = int(os.environ.get("SMTP_SSL", "0"))

EMAIL_HOST_USER = os.environ.get("SMTP_USER", "user")
EMAIL_HOST_PASSWORD = os.environ.get("SMTP_PASSWORD", "pw")

DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL",
                                    "webmaster@localhost")
SERVER_EMAIL = os.environ.get("SERVER_EMAIL", "root@localhost")

# RestFramework

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':
    ['rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS':
    'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_FILTER_BACKENDS':
    ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS':
    'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE':
    20
}

SPECTACULAR_SETTINGS = {
    'SERVERS': [{
        'url': "http://127.0.0.1:8000/"
    }],
    'COMPONENT_SPLIT_REQUEST': True,
    'VERSION': '0.0.1'
}