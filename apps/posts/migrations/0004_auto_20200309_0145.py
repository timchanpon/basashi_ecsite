# Generated by Django 3.0.4 on 2020-03-08 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200309_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='stock_amt',
            field=models.PositiveIntegerField(default=1, editable=False, verbose_name='在庫数'),
            preserve_default=False,
        ),
    ]
