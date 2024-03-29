"""
Django settings for telusko project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
# for translating between english and japanese
from django.utils.translation import gettext_lazy as _

import django
import environ

env = environ.Env()
environ.Env.read_env()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# when DEBUG=FALSE, static files won't render, need to set up nginx config
# DEBUG = False
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # this is the format to add your models for db migration
    # appname.apps.AppnameConfig
    'Art_Gallery_App.apps.Art_Gallery_AppConfig',
    'account.apps.AccountConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mathfilters',
    'phonenumber_field'
]
# if using CacheMiddleware, put LocaleMiddleware after it.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Main Project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # specify templates folder path
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Main Project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
# here you can connect with postgreSQL -- must have psycopg db adapter installed 
# here: https://pypi.org/project/psycopg2/ using pip install psycopg2 (may have to do this on multiple venv's)
# which connects django app to postgresql
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.postgresql',
        # specify database name made in pgadmin
        'NAME': 'lctec',

        # specify username and password
        # found in pgadmin, password found in postgresinfo.txt
        'USER': 'postgres',
        'PASSWORD': '2645',
        # specify which machine where db is installed
        # specify host/ip address
        'HOST': 'localhost'
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/
# the language code is the default language, change default to Japanese before deployment
# create locale folder in current directory with english and japanese subfolders
# install apt-get update then apt-get install gettext
# since this will be in Japanese, run "python manage.py makemessages -l en"
# then go translate the strings in the .po file
# then run "python manage.py compilemessages"
# see docs: https://docs.djangoproject.com/en/4.0/ref/django-admin/
# default language, change to Japanese
# list of supported languages http://www.i18nguy.com/unicode/language-identifiers.html

LANGUAGE_CODE = 'ja'



TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# for email validation and password resets
# https://www.sitepoint.com/django-send-email/
# Google uses smpt, might need to change it to a different host if using other than Google mail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = True
# email address that sends emails (make a new gmail account for Kaoru later) 
EMAIL_HOST_USER = env('EMAIL_HOST_USER') 
# EMAIL_HOST_PASSWORD generated by Google. First you have to enable 2-step verification
# Go to Google-> manage Google account -> Security -> Sigining in to Google -> App passwords ->
# click select app and choose Mail or Other -> select device name -> generate -> get password and put it in .env file
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD') 
# RECIPIENT_ADDRESS = env('RECIPIENT_ADDRESS')

EMAIL_ACTIVE_FIELD = 'is_active'
# add settings to work with static files
# specify where all static files are located
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# Django will take all static files in a Django folder
# called assets or whatever you want to name it
# go into cmd to create this assets folder
# in cmd, enter python manage.py collectstatic
# terminal will warn about overriting existing files
# enter 'yes' or 'no'
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

# creates a new media folder for static images and other media
# that you want for your models (uploading pictures as data in db)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




# get current list of languages here 
# https://github.com/django/django/blob/main/django/conf/global_settings.py
LANGUAGES = [
    ('ja', 'Japanese'),
    ('en', _('English')),
]
# location of locale folders so django can find them in directory 
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale/')
]

SESSION_EXPIRE_AT_BROWSER_CLOSE = True