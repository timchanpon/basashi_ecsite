from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """拡張ユーザーモデル"""

    user_icon = models.ImageField(verbose_name='ユーザーアイコン', upload_to='user_icon/', default='default_user_icon.jpg')

    class Meta:
        verbose_name_plural = '拡張ユーザーモデル'
