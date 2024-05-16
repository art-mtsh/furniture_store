# Generated by Django 5.0.4 on 2024-05-16 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0015_alter_itemsoftbody_sleep_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemsoftbody',
            name='armrests',
            field=models.CharField(max_length=100, null=True, verbose_name='Підлокітники'),
        ),
        migrations.AlterField(
            model_name='itemsoftbody',
            name='counter_claw',
            field=models.CharField(null=True, verbose_name='Антикіготь'),
        ),
        migrations.AlterField(
            model_name='itemsoftbody',
            name='filler',
            field=models.CharField(max_length=100, null=True, verbose_name='Наповнення'),
        ),
        migrations.AlterField(
            model_name='itemsoftbody',
            name='linen_niche',
            field=models.CharField(null=True, verbose_name='Ніша д.білизни'),
        ),
        migrations.AlterField(
            model_name='itemsoftbody',
            name='max_weight',
            field=models.IntegerField(null=True, verbose_name='Макс. навантаження'),
        ),
        migrations.AlterField(
            model_name='itemsoftbody',
            name='mechanism',
            field=models.CharField(max_length=100, null=True, verbose_name='Механізм'),
        ),
        migrations.AlterField(
            model_name='itemsoftbody',
            name='other',
            field=models.CharField(max_length=150, null=True, verbose_name='Інше'),
        ),
        migrations.AlterField(
            model_name='itemsoftbody',
            name='sleep_place',
            field=models.CharField(max_length=100, null=True, verbose_name='Спальне місце'),
        ),
        migrations.AlterField(
            model_name='itemsoftbody',
            name='springs_type',
            field=models.CharField(max_length=100, null=True, verbose_name='Пружини'),
        ),
    ]
