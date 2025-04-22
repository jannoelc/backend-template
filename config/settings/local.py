# ruff: noqa: E501
from .base import *  # noqa: F403
from .base import INSTALLED_APPS
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="LoVsgskyGdzrsQYNfi0bBWlRywlbGA6RVg06YzveyeHMU5BpbwCqCDDMW0PF7Y7a",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]  # noqa: S104

CSRF_TRUSTED_ORIGINS = ["https://localhost:5000"]
CORS_ALLOWED_ORIGINS = ["https://localhost:5000"]

# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    },
}

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = env("EMAIL_HOST", default="mailpit")
# https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = 1025

# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
if env("USE_DOCKER") == "yes":
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]

# django-extensions
# ------------------------------------------------------------------------------
# https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration
INSTALLED_APPS += ["django_extensions"]

# AUTHENTICATION
# ------------------------------------------------------------------------------
HEADLESS_FRONTEND_URLS = {
    "account_confirm_email": "https://localhost:5000/auth/verify-email/{key}",
    "account_reset_password": "https://localhost:5000/auth/password/reset",
    "account_reset_password_from_key": "https://localhost:5000/auth/password/reset/key/{key}",
    "account_signup": "https://localhost:5000/auth/signup",
    "socialaccount_login_error": "https://localhost:5000/auth/provider/callback",
}

HEADLESS_SERVE_SPECIFICATION = True

# Swagger
# ------------------------------------------------------------------------------
SPECTACULAR_SETTINGS = {
    "TITLE": "backend API",
    "DESCRIPTION": "Documentation of API endpoints of backend",
    "VERSION": "1.0.0",
    "SERVE_PERMISSIONS": [],
    "SCHEMA_PATH_PREFIX": "/api/",
}
