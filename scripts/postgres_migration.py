import os
import sys
import django
from django.core.management import call_command


def postgres_migration():
    # встановити перемінну оточення
    os.environ['ENVIRONMENT'] = 'production'
    # додати цей файл в PATH
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    # встановити перемінну оточення DJANGO_SETTINGS_MODULE
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
    # ініціалізація DJANGO
    django.setup()
    # виконання міграцій та запуску сервера
    call_command("makemigrations")
    call_command("migrate")

    print(f"Migrated with {os.environ['ENVIRONMENT']} environment!")
