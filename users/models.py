from django.db import models
from django.contrib.auth.models import AbstractUser

from posts.models import Post


class CustomUser(AbstractUser):
    """拡張ユーザーモデル"""

    user_icon = models.ImageField(verbose_name='ユーザーアイコン', default='default_user_icon.jpg')
    order_count = models.PositiveIntegerField(verbose_name='注文回数', default=0, editable=False)

    class Meta:
        verbose_name_plural = '拡張ユーザーモデル'
