"""
Django settings for project_name project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-gop3(wx!e4_g=b0t^66jtq7rnp@^#3**3*gi*(n)rqi+04v3q5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '172.30.1.9',
    '127.0.0.1'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'app_name',
    'rest_framework'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'project_name.urls'
CORS_ALLOW_ALL_ORIGINS = True
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

WSGI_APPLICATION = 'project_name.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',  # หรือ 'rest_framework.authentication.BasicAuthentication'
    ],
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',  # เพิ่มเทมเพลตนี้
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),

    # ...
}
# Database
# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nidec_drawing',
        'USER': 'odoo',
        'PASSWORD': 'odoo',
        'HOST': '172.30.1.9',
        'PORT': '5432',
        'OPTIONS': {
            'client_encoding': 'UTF8',
        }
    },
    'user_lists': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'user_list',
        'USER': 'odoo',
        'PASSWORD': 'odoo',
        'HOST': '172.30.1.9',
        'PORT': '5432',
        'OPTIONS': {
            'client_encoding': 'UTF8',
        }
    },
    'slip': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'request_slip_test',
        'USER': 'odoo',
        'PASSWORD': 'odoo',
        'HOST': '172.30.1.9',
        'PORT': '5432',
        'OPTIONS': {
            'client_encoding': 'UTF8',
        }
    },
    'setting_systems': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'setting_systems',
        'USER': 'user_setup',
        'PASSWORD': 'user_setup',
        'HOST': 'db01',
        'PORT': '5432',
        'OPTIONS': {
            'client_encoding': 'UTF8',
        }
    },
    'slip_db01': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'request_slip_test',
        'USER': 'user_setup',
        'PASSWORD': 'user_setup',
        'HOST': 'db01',
        'PORT': '5432',
        'OPTIONS': {
            'client_encoding': 'UTF8',
        }
    },
    'user_config': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'zPersonal_Rec',
        'USER': 'maker_5th',
        'PASSWORD': '5thEngineer',
        'HOST': '172.30.1.15',
        'PORT': '5432',
        'OPTIONS': {
            'client_encoding': 'UTF8',
        }
    }
}
"""
    'user_lists': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'user_list',
        'USER': 'user_setup',
        'PASSWORD': 'user_setup',
        'HOST': '172.30.1.15',
        'PORT': '5432',
        'OPTIONS': {
            'client_encoding': 'UTF8',
        }
    }
    """
MEDIA_URL = ''
MEDIA_ROOT = os.path.join(BASE_DIR, 'files')


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'onemail.one.th'
EMAIL_PORT = 465
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_HOST_USER = 'auth@nidec-precision.co.th'
EMAIL_HOST_PASSWORD = 'Nis_2022'

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3030',
    'http://127.0.0.1:5500',
    'http://172.30.1.9:8200'
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# สามารถกำหนดเพิ่มเติมตามความต้องการของคุณ
# CORS_ALLOW_HEADERS += ['your-custom-header']

# กำหนดว่า CORS ให้เข้าถึงทุกๆ โดเมน
CORS_ORIGIN_ALLOW_ALL = True
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_AGE = 360000
SESSION_SAVE_EVERY_REQUEST = True

APPEND_SLASH = False
