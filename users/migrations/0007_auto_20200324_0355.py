# Generated by Django 3.0.4 on 2020-03-23 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200324_0346'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=10, verbose_name='市区町村名')),
            ],
            options={
                'verbose_name_plural': '市区町村モデル',
            },
        ),
        migrations.CreateModel(
            name='Prefecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pref_name', models.CharField(max_length=5, verbose_name='都道府県名')),
            ],
            options={
                'verbose_name_plural': '都道府県モデル',
            },
        ),
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=models.CharField(blank=True, choices=[('新座市', '新座市'), ('西東京市', '西東京市')], max_length=5, null=True, verbose_name='市区町村'),
        ),
    ]
