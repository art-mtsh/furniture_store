# Generated by Django 5.0.4 on 2024-06-12 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_userbio_city_remove_userbio_post_office_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userbio',
            options={'ordering': ['related_user'], 'verbose_name': 'Деталі користувача', 'verbose_name_plural': 'Деталі користувачів'},
        ),
    ]
