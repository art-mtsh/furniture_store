# Generated by Django 5.0.4 on 2024-05-30 19:09

import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbio',
            name='phone',
            field=models.CharField(max_length=20, null=True, validators=[users.models.validate_phone_number], verbose_name='Телефон'),
        ),
    ]
