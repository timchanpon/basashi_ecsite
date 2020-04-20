"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.urls import path, include
from django.views.generic import RedirectView

from . import settings


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('control/', admin.site.urls),

    # tonantei_basashi
    path('', include('posts.urls')),
    path('common/', include('common.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    path('addresses/', include('addresses.urls')),
    path('orders/', include('orders.urls')),

    # belajar_hiragana
    path('belajar_hiragana/', RedirectView.as_view(url='http://bljr.ga/')),
]


# メディアを配信できるようにする設定
django_settings_module = os.environ.get('DJANGO_SETTINGS_MODULE')
if django_settings_module == 'config.settings.production':
    urlpatterns += static(settings.production.MEDIA_URL, document_root=settings.production.MEDIA_ROOT)
elif django_settings_module == 'config.settings.local':
    urlpatterns += static(settings.local.MEDIA_URL, document_root=settings.local.MEDIA_ROOT)
