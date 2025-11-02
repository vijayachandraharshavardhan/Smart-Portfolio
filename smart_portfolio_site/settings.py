import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

# ==============================
# LOAD ENV VARIABLES
# ==============================
load_dotenv()  # This loads .env file variables

# ==============================
# BASE SETTINGS
# ==============================
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv(
    'SECRET_KEY',
    '-fU_qN7LevuYVUAs6-psstfhT9jIxoHw5Kf-UTqwlx9tfWkfEOGtRjX3p7VcsswYE_dAA'
)

DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# ==============================
# INSTALLED APPS
# ==============================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local apps
    'projects',
]

# ==============================
# MIDDLEWARE
# ==============================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # for static files in production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ==============================
# SECURITY SETTINGS
# ==============================
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    X_FRAME_OPTIONS = 'DENY'
else:
    SECURE_SSL_REDIRECT = False

# ==============================
# URL CONFIG
# ==============================
ROOT_URLCONF = 'smart_portfolio_site.urls'

# ==============================
# TEMPLATES
# ==============================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
            BASE_DIR / 'projects' / 'templates',
        ],
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

# ==============================
# WSGI
# ==============================
WSGI_APPLICATION = 'smart_portfolio_site.wsgi.application'

# ==============================
# DATABASE CONFIG
# ==============================
if os.getenv('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# ==============================
# AUTHENTICATION
# ==============================
AUTH_PASSWORD_VALIDATORS = []

# ==============================
# LOCALIZATION
# ==============================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# ==============================
# STATIC & MEDIA FILES
# ==============================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'projects' / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ==============================
# DEFAULT PRIMARY KEY FIELD
# ==============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ==============================
# LOGGING
# ==============================
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
