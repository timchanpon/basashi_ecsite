from django.db import models
from django.contrib.auth.models import AbstractUser

from posts.models import Post


class CustomUser(AbstractUser):
    """拡張ユーザーモデル"""

    class Meta:
        verbose_name_plural = '拡張ユーザーモデル'


class ShoppingCart(models.Model):
    """買い物かごモデル"""

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name='ポスト', on_delete=models.CASCADE)
    order_amt = models.PositiveIntegerField(verbose_name='購入数', default=0)

    class Meta:
        verbose_name_plural = '買い物かごモデル'
