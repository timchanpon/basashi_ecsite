from django.db import models

from users.models import CustomUser


class Prefecture(models.Model):
    """都道府県モデル"""

    pref_name = models.CharField(verbose_name='都道府県名', max_length=5, unique=True)

    class Meta:
        verbose_name_plural = '１．都道府県モデル'

    def __str__(self):
        return self.pref_name


class City(models.Model):
    """市区町村モデル"""

    pref = models.ForeignKey(Prefecture, verbose_name='都道府県', on_delete=models.PROTECT)
    city_name = models.CharField(verbose_name='市区町村名', max_length=10, unique=True)

    class Meta:
        verbose_name_plural = '２．市区町村モデル'

    def __str__(self):
        pref_name = self.pref.pref_name
        city_name = self.city_name

        return pref_name + city_name


class Chome(models.Model):
    """丁目モデル"""

    city = models.ForeignKey(City, verbose_name='市区町村', on_delete=models.PROTECT)
    chome = models.CharField(verbose_name='丁目', max_length=10, unique=True)

    class Meta:
        verbose_name_plural = '３．丁目モデル'

    def __str__(self):
        pref_name = self.city.pref.pref_name
        city_name = self.city.city_name
        chome = self.chome

        return pref_name + city_name + chome


class Address(models.Model):
    """住所モデル"""

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    address_type = models.CharField(verbose_name='住所区分', max_length=10, default='自宅')
    pref = models.ForeignKey(Prefecture, verbose_name='都道府県', on_delete=models.PROTECT)
    city = models.ForeignKey(City, verbose_name='市区町村', on_delete=models.PROTECT)
    chome = models.ForeignKey(Chome, verbose_name='丁目', on_delete=models.PROTECT)
    banchi_go = models.CharField(verbose_name='番地・号', max_length=10)
    building = models.CharField(verbose_name='建物', max_length=20, blank=True, null=True)

    class Meta:
        verbose_name_plural = '住所モデル'

    def __str__(self):
        user_name = self.user.username
        address_type = self.address_type

        return user_name + ' ' + address_type
