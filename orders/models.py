from django.db import models

from users.models import CustomUser
from addresses.models import Address
from posts.models import Post


class Order(models.Model):
    """注文モデル"""

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    address = models.ForeignKey(Address, verbose_name='住所', on_delete=models.PROTECT)
    has_ended = models.BooleanField(verbose_name='終了済みか否か', default=False, editable=False)
    status = models.CharField(verbose_name='ステータス', max_length=10, blank=True, null=True)

    ordered_at = models.DateTimeField(verbose_name='注文日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    ended_at = models.DateTimeField(verbose_name='完了日時', blank=True, null=True, editable=False)

    class Meta:
        verbose_name_plural = '注文モデル'

    def __str__(self):
        user = self.user
        ordered_at = self.ordered_at
        if self.has_delivered:
            status = ' (delivered)'
        elif self.has_cancelled:
            status = ' (cancelled)'
        else:
            status = ''

        return f'{user} {ordered_at}' + status


class OrderItem(models.Model):
    """注文アイテムモデル"""

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    post = models.ForeignKey(Post, verbose_name='ポスト', on_delete=models.PROTECT)
    order = models.ForeignKey(Order, verbose_name='注文', on_delete=models.PROTECT, blank=True, null=True, editable=False)
    order_amt = models.PositiveIntegerField(verbose_name='購入数', default=0)
    in_cart = models.BooleanField(verbose_name='買い物かごの中か否か', default=True, editable=False)

    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = '注文アイテムモデル'

    def __str__(self):
        user = self.user
        post = self.post
        order_amt = self.order_amt
        if self.in_cart:
            status = ' (in_cart)'
        else:
            status = ''

        return f'{user} {post} {order_amt}個' + status
