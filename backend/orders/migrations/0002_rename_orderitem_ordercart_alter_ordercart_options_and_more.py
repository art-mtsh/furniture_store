# Generated by Django 5.0.4 on 2024-06-02 19:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0023_rename_category_items_item_category'),
        ('orders', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderItem',
            new_name='OrderCart',
        ),
        migrations.AlterModelOptions(
            name='ordercart',
            options={'ordering': ['related_user'], 'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзина'},
        ),
        migrations.AlterModelTable(
            name='ordercart',
            table='order_cart',
        ),
    ]
