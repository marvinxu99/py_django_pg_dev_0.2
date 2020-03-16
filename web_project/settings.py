"""
Django settings for web_project project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import environ
import django_heroku

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
env.read_env()   # reading .env file

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "CHANGE_ME!!!! (P.S. the SECRET_KEY environment variable will be used, if set, instead)."
# SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ.get("ENVIRONMENT") == "PROD":
    DEBUG = False
    DOMAIN = 'PROD'
else:
    DEBUG = True
    DOMAIN = 'DEV'

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',    # http://whitenoise.evans.io/en/stable/django.html
    'django.contrib.staticfiles',
    'polls.apps.PollsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',    # http://whitenoise.evans.io/en/stable/
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'web_project.urls'

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

WSGI_APPLICATION = 'web_project.wsgi.application'

# Email backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
if os.environ.get("ENVIRONMENT") == "PROD":
    EMAIL_HOST_USER = os.environ.get('MY_GMAIL')
    EMAIL_HOST_PASSWORD = os.environ.get('MY_GMAIL_PASSWORD')
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    # EMAIL_USE_SSL = True
    # EMAIL_PORT = 465
else:
    EMAIL_HOST_USER = env.str('MY_GMAIL')
    EMAIL_HOST_PASSWORD = env.str('MY_GMAIL_PASSWORD')
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    # EMAIL_USE_SSL = True
    # EMAIL_PORT = 465


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# mysql wheels: https://www.lfd.uci.edu/~gohlke/pythonlibs/
# postgreSQL: https://docs.djangoproject.com/en/3.0/ref/databases/

if os.environ.get("ENVIRONMENT") == "PROD":  
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'winndb_poll_prod',
            'USER': 'winter',
            'PASSWORD': 'winter',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
else: 
    DATABASES = {
        # 'default': {
        #     'ENGINE': 'django.db.backends.sqlite3',
        #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # }

        # 'default': {
        #     'ENGINE': 'django.db.backends.mysql',
        #     'NAME': 'winndb_poll',
        #     'USER': 'winter',
        #     'PASSWORD': 'winter',
        #     'HOST': 'localhost',
        #     'PORT': '',
        #     # 'OPTIONS': {
        #     #     'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        #     #     }
        # }

        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'winndb_poll_dev',
            'USER': 'winter',
            'PASSWORD': 'winter',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'US/Pacific'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static_collected')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'   # http://whitenoise.evans.io/en/stable/django.html
# http://whitenoise.evans.io/en/stable/django.html#storage-troubleshoot
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# addin the following will cause HEROU rejected to deploy????
# but works locally???heroku
if os.environ.get("ENVIRONMENT") != "PROD":
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
        os.path.join(BASE_DIR, "generated_codes"),
    ]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

FILE_UPLOAD_TEMP_DIR = os.path.join(BASE_DIR, 'uploaded_files_temp')

# Configure Django App for Heroku. 
django_heroku.settings(locals())
