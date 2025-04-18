from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "your-secret-key-here"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
import os

STATIC_URL = "/static/"
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]  # Make sure this folder exists
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")  # Collects all static files here


ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Application definition
INSTALLED_APPS = [
 'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # My apps
    'rest_api',
    

       
       
    # Third-party apps
    'rest_framework',
    'rest_framework.authtoken',
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

ROOT_URLCONF = 'drfcore.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "rest_api/templates")],  # Custom template directory
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


WSGI_APPLICATION = 'drfcore.wsgi.application'

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "estdb",
        "USER": "estf",
        "PASSWORD": "password10q",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True



# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    "site_title": "Book Store",
    "site_header": "Book Store",
    "site_brand": "Book Store",
    "welcome_sign": "Welcome to Book Store Dashboard",
    "site_logo": "rest_api/images/logo.jpg",  # Place logo inside static/rest_api/images/
    "login_logo": "rest_api/images/logo.jpg",
    "copyright": "© 2025 Django-Rest",
    "search_model": "rest_api.Customer",  # Change 'MyModel' to any model in rest_api

    # Theme Settings
    "theme": "pulse",  # Options: flatly, minty, pulse, superhero, etc.

    # Custom CSS & JS
    "custom_css": "css/custom_admin.css",
    "custom_js": "js/custom_admin.js",

    # Top Menu Links
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"app": "rest_api"},
    ],

    # Sidebar Customization
    "side_menu": [
        {"app": "rest_api", "name": "REST API Management", "models": [
            "rest_api.Customer",  # Replace with actual model names
            "rest_api.Post",
        ]},
    ],

    # Icons for models
    "icons": {
        "rest_api.Customer": "fas fa-database",  # Use FontAwesome icons
        "rest_api.Post": "fas fa-cogs",
        "auth.user": "fas fa-user",
    },
}

JAZZMIN_SETTINGS["custom_css"] = "css/custom_admin.css"
JAZZMIN_SETTINGS["login_logo"] = "rest_api/images/logo.jpg"
JAZZMIN_SETTINGS["login_background"] = "rest_api/images/logo.png"
JAZZMIN_SETTINGS["custom_js"] = "js/custom_admin.js"
# JAZZMIN_SETTINGS["site_logo"] = "rest_api/images/logo.png"


