from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dnr6k*zeno30^)b!d6l_f@)%%ry@bm^hcv0+7a2c^_o88@++z2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# 開発環境でのメール送信先設定
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
