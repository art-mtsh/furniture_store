# Generated by Django 5.0.4 on 2024-06-04 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_userfavorites_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbio',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userbio',
            name='post_office',
        ),
        migrations.RemoveField(
            model_name='userbio',
            name='state',
        ),
    ]
