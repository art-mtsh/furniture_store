# Generated by Django 5.0.4 on 2024-05-16 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0014_alter_itemsoftbody_counter_claw_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemsoftbody',
            name='sleep_size',
            field=models.CharField(max_length=100, null=True, verbose_name='Спальне місце ДхШ'),
        ),
    ]