# Generated by Django 3.0.4 on 2020-03-30 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_orderitem_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='has_cancelled',
        ),
        migrations.RemoveField(
            model_name='order',
            name='has_delivered',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='ordered', max_length=10, verbose_name='ステータス'),
        ),
    ]
