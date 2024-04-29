# Generated by Django 5.0.4 on 2024-04-28 22:03

import api.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Категорія')),
            ],
            options={
                'verbose_name': "Категорія об'єкта",
                'verbose_name_plural': "Категорії об'єкта",
                'db_table': 'api_item_category',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='ItemCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Колекція')),
            ],
            options={
                'verbose_name': 'Колекція',
                'verbose_name_plural': 'Колекції',
                'db_table': 'api_collection',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='ItemColour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Колекція')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Семпл кольору')),
            ],
            options={
                'verbose_name': 'Колір',
                'verbose_name_plural': 'Кольори',
                'db_table': 'api_colours',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='ItemMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Матеріал')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Семпл дерева')),
            ],
            options={
                'verbose_name': 'Дерево',
                'verbose_name_plural': 'Дерево',
                'db_table': 'api_woods',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Назва товару')),
                ('article_code', models.IntegerField(unique=True, verbose_name='Артикул')),
                ('price', models.FloatField(verbose_name='Ціна, ГРН')),
                ('upholstery_material', models.CharField(blank=True, max_length=150, verbose_name='Наповнення')),
                ('upholstery_capacity', models.IntegerField(blank=True, verbose_name='Щільність набивки')),
                ('d_length', models.IntegerField(blank=True, verbose_name='Загальна довжина')),
                ('d_width', models.IntegerField(blank=True, verbose_name='Загальна ширина')),
                ('d_height', models.IntegerField(blank=True, verbose_name='Загальна висота')),
                ('dimension_in_use_length', models.IntegerField(blank=True, verbose_name='Корисна довжина')),
                ('dimension_in_use_width', models.IntegerField(blank=True, verbose_name='Корисна ширина')),
                ('dimension_in_use_height', models.IntegerField(blank=True, verbose_name='Загальна висота')),
                ('counter_claw', models.BooleanField(default=False, verbose_name='Захист від кігтів')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Створено')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Відредаговано')),
                ('is_published', models.BooleanField(default=True, verbose_name='Статус публікації')),
                ('collection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.itemcollection', verbose_name='Колекція')),
                ('item_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.itemcategory', verbose_name='Категорія')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товари',
                'db_table': 'api_items',
                'ordering': ['room_type', 'item_category', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Виробник')),
                ('about', models.TextField(blank=True, verbose_name='Інформація про виробника')),
            ],
            options={
                'verbose_name': 'Виробник',
                'verbose_name_plural': 'Виробники',
                'db_table': 'api_manufacturer',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото товару')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фото',
                'db_table': 'api_photos',
                'ordering': ['item'],
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name="Ім'я")),
                ('second_name', models.CharField(max_length=150, verbose_name='Прізвище')),
                ('rating', models.IntegerField(validators=[api.models.validate_even], verbose_name='Оцінка товару')),
                ('review_usefulness_counter', models.IntegerField(default=0, verbose_name='Корисність відгуку')),
            ],
            options={
                'verbose_name': 'Відгук',
                'verbose_name_plural': 'Відгуки',
                'db_table': 'api_reviews',
                'ordering': ['item'],
            },
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Тип кімнати')),
            ],
            options={
                'verbose_name': 'Тип кімнати',
                'verbose_name_plural': 'Типи кімнат',
                'db_table': 'api_room_type',
                'ordering': ['title'],
            },
        ),
        migrations.DeleteModel(
            name='TestTextModel',
        ),
        migrations.AddField(
            model_name='itemmaterial',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.items', verbose_name='Товар'),
        ),
        migrations.AddField(
            model_name='itemcolour',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.items', verbose_name='Товар'),
        ),
        migrations.AddField(
            model_name='items',
            name='manufacturer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.manufacturer', verbose_name='Виробник'),
        ),
        migrations.AddField(
            model_name='itemcollection',
            name='manufacturer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.manufacturer', verbose_name='Виробник'),
        ),
        migrations.AddField(
            model_name='photos',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.items', verbose_name='Товар'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='get_news', to='api.items', verbose_name='Товар'),
        ),
        migrations.AddField(
            model_name='items',
            name='room_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.roomtype', verbose_name='Тип кімнати'),
        ),
        migrations.AddField(
            model_name='itemcategory',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.roomtype', verbose_name='Тип кімнати'),
        ),
    ]
