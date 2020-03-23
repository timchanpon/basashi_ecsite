# Generated by Django 3.0.4 on 2020-03-23 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_part'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='part',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='posts.Part', verbose_name='部位'),
            preserve_default=False,
        ),
    ]
