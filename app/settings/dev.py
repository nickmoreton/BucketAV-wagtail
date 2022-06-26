from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-n*x8mrjfk^rs_064fgpre5_pwb(g_xxzw$u*tr6^uyim!lqz^#"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

CSRF_TRUSTED_ORIGINS = ["https://*.gitpod.io"]

INSTALLED_APPS += [  # noqa: F405
    "wagtail.contrib.styleguide",
    "django_extensions",
]

try:
    from .local import *
except ImportError:
    pass
