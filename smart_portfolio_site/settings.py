import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

# ==============================
# BASE DIRECTORY
# ==============================
BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================
# LOAD ENV VARIABLES
# ==============================
# Load .env only in local dev; in Render we use Environment Secrets
dotenv_path = BASE_DIR / ".env"
if dotenv_path.exists():
    load_dotenv(dotenv_path)

# ==============================
# CORE SETTINGS
# ==============================
SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret-key-for-local")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# ==============================
# ALLOWED HOSTS
# ==============================
# Read from environment variable
ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS",
    "127.0.0.1,localhost,smart-portfolio-ogp7.onrender.com"
).split(",")
# Clean up spaces
ALLOWED_HOSTS = [host.strip() for host in ALLOWED_HOSTS if host.strip()]

# ==============================
# INSTALLED APPS
# ==============================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "projects",  # Local app
    "cloudinary_storage",
    "cloudinary",
]

# ==============================
# MIDDLEWARE
# ==============================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # serve static files
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
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
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    X_FRAME_OPTIONS = "DENY"
else:
    SECURE_SSL_REDIRECT = False

# ==============================
# URL CONFIG
# ==============================
ROOT_URLCONF = "smart_portfolio_site.urls"

# ==============================
# TEMPLATES
# ==============================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates", BASE_DIR / "projects" / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ==============================
# WSGI
# ==============================
WSGI_APPLICATION = "smart_portfolio_site.wsgi.application"

# ==============================
# DATABASE
# ==============================
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.parse(DATABASE_URL, conn_max_age=600)
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# ==============================
# PASSWORD VALIDATORS
# ==============================
AUTH_PASSWORD_VALIDATORS = []

# ==============================
# LOCALIZATION
# ==============================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_TZ = True

# ==============================
# STATIC & MEDIA
# ==============================
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "projects" / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# Cloudinary settings
import cloudinary
import cloudinary.uploader
import cloudinary.api

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.getenv('CLOUDINARY_API_KEY'),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET'),
}

cloudinary.config(**CLOUDINARY_STORAGE)

# Ensure uploads use permanent public URLs, not expiring authenticated ones
cloudinary.uploader.default_upload_options = {'type': 'upload'}

# Use Cloudinary for media files
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"  # Fallback for local development

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ==============================
# DEFAULT AUTO FIELD
# ==============================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ==============================
# LOGGING
# ==============================
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },
    "root": {"handlers": ["console"], "level": "INFO"},
}

# ==============================
# DEBUG INFO (optional)
# ==============================
print(f"DEBUG={DEBUG}")
print(f"ALLOWED_HOSTS={ALLOWED_HOSTS}")
