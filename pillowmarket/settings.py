"""
Django settings for pillowmarket project.

Generated by 'django-admin startproject' using Django 2.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import json
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
with open(os.path.join(BASE_DIR, 'json/secret.json'), 'r') as secret_file:
    secret_value = json.load(secret_file)
SECRET_KEY = secret_value["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainapp',
    'compressor',  # for connect 'sass'
    'appconf',  # for connect 'sass'
    'authapp',
    'basketapp',
    'adminapp',
    'social_django',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware'
]

ROOT_URLCONF = 'pillowmarket.urls'

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
                'mainapp.context_processors.get_basket_itm',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect'
            ],
        },
    },
]

WSGI_APPLICATION = 'pillowmarket.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

#  ============  for connect 'sass'  ===================

STATICFILES_FINDERS = (
    # default
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'sass'
    'compressor.finders.CompressorFinder',
)

COMPRESS_ENABLED = True

COMPRESS_ROOT = os.path.join(BASE_DIR, '../static/')

# =======================================================


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# используем своё приложение для аутентификации
AUTH_USER_MODEL = 'authapp.Buyer'

LOGIN_URL = '/auth/login/'

# корректно обработаем ошибку об отказе доп. обрабатывать данные пользователя
# при запросе из соц сетей
LOGIN_ERROR_URL = '/'

DOMAIN_NAME = 'http://localhost:8000'

EMAIL_HOST = 'localhost'
# EMAIL_HOST_USER = 'django@geekshop.local'
# EMAIL_HOST_PASSWORD = 'geekshop'
EMAIL_PORT = '7725'
EMAIL_USE_SSL = False

# пример использования yandex
# EMAIL_HOST = 'smtp.yandex.ru'
# EMAIL_HOST_USER = 'qwerty@yandex.ru'
# EMAIL_HOST_PASSWORD = 'password'
# EMAIL_PORT = '465'
# EMAIL_USE_SSL = True

# вариант запуска локального smtp сервера: python3 -m smtpd -n -c DebuggingServer localhost:7725
EMAIL_HOST_USER, EMAIL_HOST_PASSWORD = None, None

# вариант логгирования сообщений почты ввиде файлов
# EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
# EMAIL_FILE_PATH = 'tmp/email-messages/'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # встроенный бэкенд
    'social_core.backends.vk.VKOAuth2',  # вк бэкенд
    'social_core.backends.google.GoogleOAuth2',  # google бэкенд
)

SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_VK_OAUTH2_KEY = secret_value['SOCIAL_AUTH_VK_OAUTH2_KEY']
SOCIAL_AUTH_VK_OAUTH2_SECRET = secret_value['SOCIAL_AUTH_VK_OAUTH2_SECRET']

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = secret_value['SOCIAL_AUTH_GOOGLE_OAUTH2_KEY']  # Google Consumer Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = secret_value['SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET']  # Google Consumer Secret

# отключаем запрос данных из VK по умолчанию
SOCIAL_AUTH_VK_OAUTH2_IGNORE_DEFAULT_SCOPE = True
# выбираем поля данных из VK, которые запросим
SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email']

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.create_user',
    # добавляем в конвеер свой метод, последовательно после создания польз.-ля
    'authapp.pipeline.save_buyer_profile',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)
