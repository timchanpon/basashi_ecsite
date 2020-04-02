from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# 開発環境でのメール送信先設定
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
