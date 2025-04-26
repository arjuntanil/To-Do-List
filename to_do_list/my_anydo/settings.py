# my_anydo/settings.py

import os
from pathlib import Path

# Base directory for the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret Key (keep it secret in production)
SECRET_KEY = 'your-secret-key-here'

# Debug mode (set to False in production)
DEBUG = True

# Allowed hosts (add your domain if in production)
ALLOWED_HOSTS = []

# Installed apps (including your app 'tasks')
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks',  # Your tasks app
    'crispy_forms',  # Optional, for better form styling
]

# Middleware to handle requests and responses
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL configuration
ROOT_URLCONF = 'my_anydo.urls'

# Template settings (configuring HTML files to be loaded from `templates/` folder)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# WSGI application for the project
WSGI_APPLICATION = 'my_anydo.wsgi.application'

# Database configuration (using SQLite in development)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Default database path
    }
}


# Password validation settings for user security
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization (set your language and timezone)
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

# Static files (CSS, JavaScript, images)
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

LOGIN_URL = 'login'  # This should match the name of your login URL pattern
# Login redirect URL (where to redirect after login)
LOGIN_REDIRECT_URL = 'index'  # Redirect to home page after successful login

# Logout redirect URL (where to redirect after logout)
LOGOUT_REDIRECT_URL = 'login'  # Redirect to login page after logout

# The default auto field type for primary keys
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# User authentication settings
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Default authentication backend
]

# Email backend (useful for sending emails in production)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Default for development
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'robinskroy600@gmail.com'  # Replace with your email
EMAIL_HOST_PASSWORD = 'ujwe hady qtrn hskw' 
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
[
    
]

# Static file management (production setup)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Collect static files in this directory

# Crispy forms configuration (optional for form rendering)
CRISPY_TEMPLATE_PACK = 'bootstrap4'  # Uses Bootstrap 4 for styling forms
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

SESSION_COOKIE_AGE = 300  # Session valid for 300 seconds (5 minutes)
