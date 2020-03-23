from django.db import models
from django.contrib.auth.models import AbstractUser

from posts.models import Post


class Prefecture(models.Model):
    """都道府県モデル"""

    pref_name = models.CharField(verbose_name='都道府県名', max_length=5)

    class Meta:
        verbose_name_plural = '都道府県モデル'

    def __str__(self):
        return self.pref_name


class City(models.Model):
    """市区町村モデル"""

    pref = models.ForeignKey(Prefecture, verbose_name='都道府県', on_delete=models.CASCADE)
    city_name = models.CharField(verbose_name='市区町村名', max_length=10)

    class Meta:
        verbose_name_plural = '市区町村モデル'

    def __str__(self):
        pref_name = self.pref.pref_name
        city_name = self.city_name

        return pref_name + city_name


class Chome(models.Model):
    """丁目モデル"""

    city = models.ForeignKey(City, verbose_name='市区町村', on_delete=models.CASCADE)
    chome = models.CharField(verbose_name='丁目', max_length=10)

    class Meta:
        verbose_name_plural = '丁目モデル'

    def __str__(self):
        pref_name = self.city.pref.pref_name
        city_name = self.city.city_name
        chome = self.chome

        return pref_name + city_name + chome


class CustomUser(AbstractUser):
    """拡張ユーザーモデル"""

    pref = models.ForeignKey(Prefecture, verbose_name='都道府県', on_delete=models.CASCADE, blank=True, null=True)
    city = models.ForeignKey(City, verbose_name='市区町村', on_delete=models.CASCADE, blank=True, null=True)
    chome = models.ForeignKey(Chome, verbose_name='丁目', on_delete=models.CASCADE, blank=True, null=True)
    banchi_go = models.CharField(verbose_name='番地・号', max_length=10, blank=True, null=True)
    building = models.CharField(verbose_name='建物', max_length=20, blank=True, null=True)
    address = models.CharField(verbose_name='住所', max_length=55, editable=False, blank=True, null=True)

    class Meta:
        verbose_name_plural = '拡張ユーザーモデル'


class ShoppingCart(models.Model):
    """買い物かごモデル"""

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name='ポスト', on_delete=models.CASCADE)
    order_amt = models.PositiveIntegerField(verbose_name='購入数', default=0)

    class Meta:
        verbose_name_plural = '買い物かごモデル'

    def __str__(self):
        user = self.user
        post = self.post
        order_amt = self.order_amt

        return f'{user} {post} {order_amt}個'
