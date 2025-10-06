import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# ✅ Directly use your API key (replace with your actual key)
GEMINI_API_KEY = "AIzaSyBdN_vb4CH643a7pN1gCUcEHiDD8myLEoo"

# Django secret key (hardcoded for now since no .env)
SECRET_KEY = "dev-secret-key"

DEBUG = True

ALLOWED_HOSTS = ['*']  # ✅ Allow all hosts (important especially on Android / Pydroid)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Chatbot',   # ✅ Your Chatbot app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Chat_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "Chatbot" / "templates"],  # ✅ Correct
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

WSGI_APPLICATION = 'Chat_project.wsgi.application'

# ✅ Even though no database is used, leave default SQLite to avoid errors
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'

# ✅ Keep only one TIME_ZONE -- you accidentally declared it twice earlier

TIME_ZONE = 'UTC'

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'Chatbot'/"static"]
STATIC_ROOT = BASE_DIR / "staticfiles"