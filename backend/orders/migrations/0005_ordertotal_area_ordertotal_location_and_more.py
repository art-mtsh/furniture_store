# Generated by Django 5.0.4 on 2024-06-04 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_ordertotal_items_ordertotal_order_sum_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordertotal',
            name='area',
            field=models.CharField(default=None, verbose_name='Тип'),
        ),
        migrations.AddField(
            model_name='ordertotal',
            name='location',
            field=models.CharField(default=None, verbose_name='Нп'),
        ),
        migrations.AddField(
            model_name='ordertotal',
            name='location_type',
            field=models.CharField(default=None, verbose_name='Тип нп'),
        ),
        migrations.AddField(
            model_name='ordertotal',
            name='region',
            field=models.CharField(default=None, verbose_name='Область'),
        ),
        migrations.AddField(
            model_name='ordertotal',
            name='warehouse',
            field=models.IntegerField(default=None, verbose_name='Склад'),
        ),
        migrations.AlterField(
            model_name='ordertotal',
            name='status',
            field=models.CharField(default='В обробці', verbose_name='Статус'),
        ),
    ]
