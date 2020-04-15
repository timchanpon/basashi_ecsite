from django.db import models


class SiteSettings(models.Model):
    """サイト設定モデル"""

    site_name = models.CharField(verbose_name='サイト名', max_length=10, unique=True)
    is_selected = models.BooleanField(verbose_name='有効化', default=False, unique=True)

    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'サイト設定モデル'

    def __str__(self):
        return self.site_name
