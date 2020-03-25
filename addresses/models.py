from django.db import models

from users.models import CustomUser


class Address(models.Model):
    """住所モデル"""

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    address_type = models.CharField(verbose_name='住所区分', max_length=10, default='自宅')
    pref = models.CharField(verbose_name='都道府県', max_length=5)
    city = models.CharField(verbose_name='市区町村', max_length=10)
    chome = models.CharField(verbose_name='丁目', max_length=15)
    banchi_go = models.CharField(verbose_name='番地・号', max_length=10)
    building = models.CharField(verbose_name='建物', max_length=30, blank=True, null=True)

    class Meta:
        verbose_name_plural = '住所モデル'

    def __str__(self):
        user_name = self.user.username
        address_type = self.address_type

        return user_name + ' ' + address_type
