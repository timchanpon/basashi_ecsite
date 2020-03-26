from django.db import models

from users.models import CustomUser
from posts.models import Post


class Order(models.Model):
    """注文モデル"""

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name='ポスト', on_delete=models.CASCADE)
    order_amt = models.PositiveIntegerField(verbose_name='購入数', default=0)
    status = models.CharField(verbose_name='ステータス', max_length=10, default='in_cart', editable=False)

    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = '注文モデル'

    def __str__(self):
        user = self.user
        post = self.post
        order_amt = self.order_amt
        status = self.status

        return f'{user} {post} {order_amt}個 ({status})'
