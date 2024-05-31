# Generated by Django 5.0.4 on 2024-05-30 13:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0023_rename_category_items_item_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(null=True, verbose_name='Телефон')),
                ('birth_date', models.DateField(null=True, verbose_name='Дата народження')),
                ('state', models.CharField(null=True, verbose_name='Область')),
                ('city', models.CharField(null=True, verbose_name='Місто')),
                ('post_office', models.CharField(null=True, verbose_name='Відділення НовоїПошти')),
                ('related_user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Користувач')),
            ],
            options={
                'verbose_name': 'Деталі користувача',
                'verbose_name_plural': 'Деталі користувача',
                'db_table': 'user_bio',
                'ordering': ['related_user'],
            },
        ),
        migrations.CreateModel(
            name='UserFavorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('related_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.items', verbose_name='Товар')),
                ('related_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Користувач')),
            ],
            options={
                'verbose_name': 'Обране',
                'verbose_name_plural': 'Обрані',
                'db_table': 'user_favorites',
                'ordering': ['related_user'],
            },
        ),
    ]