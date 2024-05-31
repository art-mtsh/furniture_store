from pathlib import Path
import os

# для jwt
from datetime import timedelta

# для екстернал зберігання credentials
from dotenv import load_dotenv

# завантажити файл .env з credentials в ньому
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$6ia5gsw+$7q_@zljh0&udxb_(+50v^^4*amgf3aom!*lkl+=w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# додані виключення та параметр DEFAULT_SCHEMA_CLASS поки що використовуються за замовчуванням
REST_FRAMEWORK = {
    # 'EXCEPTION_HANDLER': 'backend.utils.custom_exception_handler',
    # "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.openapi.SchemaGenerator",
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework_simplejwt.authentication.JWTAuthentication",),
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny", ],
}
# rest_framework.permissions.AllowAny - за замовчуванням credentials не питаємо, необхідність визначаємо самим view


# час життя JWT токена
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "drf_spectacular",
    'rest_framework',
    "corsheaders",
    'items',
    'users',
    'orders',
    'debug_toolbar',
]
# заголовки для CORS => corsheaders
# як і MIDDLEWARE corsheaders.middleware.CorsMiddleware:
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
INTERNAL_IPS = [
    '127.0.0.1',
]

# шукає глобальну змінну 'ENVIRONMENT', якщо її нема встановлює 'development'
# ENVIRONMENT = os.environ.get('ENVIRONMENT', "Development")
ENVIRONMENT = 'production'

# таким чином розділяємо тестову та продакшн БД
# ПОСЛІДОВНИЙ ЗАПУСК НЕ ПРАЦЮЄ!!!
if ENVIRONMENT == 'production':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': os.getenv('DB_PORT'),
        }
    }
# else:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': BASE_DIR / 'db.sqlite3',
#         }
#     }

CORS_ALLOW_ALL_ORIGINS = True  # відключити на прод
CORS_ALLOWS_CREDENTIALS = True
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
]

ROOT_URLCONF = 'backend.urls'

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

# SECURE_SSL_REDIRECT = True

WSGI_APPLICATION = 'backend.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,

    'formatters': {
        'custom_format': {
            'format': '886c2329-fe6c-4529-a321-e65c6742dd94:%(message)s'
        },
    },

    "handlers": {
        "sematext": {
            "level": "DEBUG",
            "class": "logging.handlers.SysLogHandler",
            "address": ("logsene-syslog-receiver.eu.sematext.com", 514),
            "formatter": "custom_format"
        },
    },

    "loggers": {
        "HelloLogs": {
            'level': 'DEBUG',
            'handlers': ['sematext'],  # Add the file handler here
            'propagate': False,
        }
    },
}

from google.oauth2 import service_account
import json

GS_CREDENTIALS_JSON = os.getenv('CREDENTIALS_JSON')
GS_CREDENTIALS = service_account.Credentials.from_service_account_info(json.loads(GS_CREDENTIALS_JSON))
DEFAULT_FILE_STORAGE = 'backend.gcloud.GoogleCloudMediaFileStorage'
GS_PROJECT_ID = os.getenv('GS_PROJECT_ID')
GS_BUCKET_NAME = os.getenv('GS_BUCKET_NAME')
MEDIA_URL = f'https://storage.googleapis.com/{GS_BUCKET_NAME}/'
