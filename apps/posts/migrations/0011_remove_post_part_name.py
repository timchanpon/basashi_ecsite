# Generated by Django 3.0.4 on 2020-03-23 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_post_part'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='part_name',
        ),
    ]
