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
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.urls import path, include

from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('posts.urls')),
    path('common/', include('common.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    path('addresses/', include('addresses.urls')),
    path('orders/', include('orders.urls')),
]


# 開発サーバーでメディアを配信できるようにする設定
urlpatterns += static(settings.local.MEDIA_URL, document_root=settings.local.MEDIA_ROOT)
