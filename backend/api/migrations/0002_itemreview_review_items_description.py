# Generated by Django 5.0.4 on 2024-04-30 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemreview',
            name='review',
            field=models.TextField(blank=True, verbose_name='Відгук'),
        ),
        migrations.AddField(
            model_name='items',
            name='description',
            field=models.TextField(blank=True, verbose_name='Опис товару'),
        ),
    ]
