# Generated by Django 3.0.4 on 2020-03-29 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0014_auto_20200326_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_delivered', models.BooleanField(default=False, editable=False, verbose_name='配達済みか否か')),
                ('has_cancelled', models.BooleanField(default=False, editable=False, verbose_name='キャンセル済みか否か')),
                ('ordered_at', models.DateTimeField(auto_now_add=True, verbose_name='注文日時')),
                ('ended_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='完了日時')),
            ],
            options={
                'verbose_name_plural': '注文モデル',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_amt', models.PositiveIntegerField(default=0, verbose_name='購入数')),
                ('in_cart', models.BooleanField(default=True, editable=False, verbose_name='買い物かごの中か否か')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='posts.Post', verbose_name='ポスト')),
            ],
            options={
                'verbose_name_plural': '注文アイテムモデル',
            },
        ),
    ]