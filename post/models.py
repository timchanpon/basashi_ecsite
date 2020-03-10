from django.db import models


class Post(models.Model):
    """ポストモデル"""

    part_name = models.CharField(verbose_name='部位名', max_length=20)
    details = models.TextField(verbose_name='詳細', max_length=200, blank=True, null=True)
    image = models.ImageField(verbose_name='商品画像', default='basashi_sample.jpg')
    num_grams = models.PositiveIntegerField(verbose_name='グラム数', default=100)
    purchase_amt = models.PositiveIntegerField(verbose_name='仕入れ量', default=1)
    stock_amt = models.PositiveIntegerField(verbose_name='在庫数', editable=False)

    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'ポストモデル'

    def __str__(self):
        return self.part_name
