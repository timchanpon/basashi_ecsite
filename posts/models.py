from django.db import models
from django.utils import timezone


class Part(models.Model):
    """部位モデル"""

    part_name = models.CharField(verbose_name='部位名', max_length=20)
    how_to_eat = models.TextField(verbose_name='賞味方法', max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = '部位モデル'

    def __str__(self):
        return self.part_name


class Post(models.Model):
    """ポストモデル"""

    part = models.ForeignKey(Part, verbose_name='部位', on_delete=models.CASCADE)
    part_name = models.CharField(verbose_name='部位名', max_length=20)
    details = models.TextField(verbose_name='詳細', max_length=200, blank=True, null=True)
    image = models.ImageField(verbose_name='商品画像', default='basashi_sample.jpg')
    num_grams = models.PositiveIntegerField(verbose_name='グラム数', default=100)
    price = models.PositiveIntegerField(verbose_name='価格')
    purchase_amt = models.PositiveIntegerField(verbose_name='仕入れ量', default=1)
    stock_amt = models.PositiveIntegerField(verbose_name='在庫数', editable=False)
    exp_date = models.DateField(verbose_name='商品期限', default=timezone.now)

    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'ポストモデル'

    def __str__(self):
        return self.part_name
