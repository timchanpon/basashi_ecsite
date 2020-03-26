from django.db import models
from django.contrib.auth.models import AbstractUser

from posts.models import Post


class CustomUser(AbstractUser):
    """拡張ユーザーモデル"""

    user_icon = models.ImageField(verbose_name='ユーザーアイコン', default='default_user_icon.jpg')
    order_count = models.PositiveIntegerField(verbose_name='注文回数', default=0, editable=False)

    class Meta:
        verbose_name_plural = '拡張ユーザーモデル'


class ShoppingCart(models.Model):
    """買い物かごモデル"""

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name='ポスト', on_delete=models.CASCADE)
    order_amt = models.PositiveIntegerField(verbose_name='購入数', default=0)

    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = '買い物かごモデル'

    def __str__(self):
        user = self.user
        post = self.post
        order_amt = self.order_amt

        return f'{user} {post} {order_amt}個'
