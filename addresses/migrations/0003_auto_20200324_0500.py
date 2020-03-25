# Generated by Django 3.0.4 on 2020-03-23 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0002_auto_20200324_0456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chome',
            name='chome',
            field=models.CharField(max_length=10, unique=True, verbose_name='丁目'),
        ),
        migrations.AlterField(
            model_name='city',
            name='city_name',
            field=models.CharField(max_length=10, unique=True, verbose_name='市区町村名'),
        ),
        migrations.AlterField(
            model_name='prefecture',
            name='pref_name',
            field=models.CharField(max_length=5, unique=True, verbose_name='都道府県名'),
        ),
    ]