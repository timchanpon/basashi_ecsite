# Generated by Django 3.0.4 on 2020-03-26 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20200326_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='order_count',
            field=models.PositiveIntegerField(default=0, editable=False, verbose_name='注文回数'),
        ),
    ]
