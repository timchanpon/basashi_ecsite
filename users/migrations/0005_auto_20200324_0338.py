# Generated by Django 3.0.4 on 2020-03-23 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customuser_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='address',
        ),
        migrations.AddField(
            model_name='customuser',
            name='city',
            field=models.CharField(blank=True, choices=[('新座市', '新座市'), ('西東京市', '西東京市')], max_length=5, null=True, verbose_name='市町村'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='pref',
            field=models.CharField(blank=True, choices=[('埼玉県', '埼玉県'), ('東京都', '東京都')], max_length=3, null=True, verbose_name='都道府県'),
        ),
    ]
