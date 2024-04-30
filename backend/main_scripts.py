import os
import sys
import django
import platform
from django.core.management import call_command


def sqlite_migration():
    os.environ['ENVIRONMENT'] = 'development'
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
    django.setup()
    call_command("makemigrations")
    call_command("migrate")
    print(f"Migrated with {os.environ['ENVIRONMENT']} environment!")

def postgres_migration():
    os.environ['ENVIRONMENT'] = 'production'
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
    django.setup()
    call_command("makemigrations")
    call_command("migrate")
    print(f"Migrated with {os.environ['ENVIRONMENT']} environment!")

def run_local_server():
    sqlite_migration()
    call_command("runserver", ["127.0.0.1:8000", "--noreload"])


def run_prod_server():
    postgres_migration()
    call_command("runserver", ["0.0.0.0:8000", "--noreload"])

#
# def set_environment():
#     """
#     Визначаємо де ми знаходимось
#     :return: "development" or "production"
#     """
#
#     if platform.node() == "DESKTOP-5PMV5U1":
#
#         os.environ['ENVIRONMENT'] = 'development'
#         os.environ['IP_ADDRESS'] = 'localhost:8000'
#     else:
#         os.environ['ENVIRONMENT'] = 'production'
#         os.environ['IP_ADDRESS'] = '0.0.0.0:8000'
#
#
# def main():
#     # виконати усі міграції для тестового сервера
#     os.environ['ENVIRONMENT'] = 'development'
#     sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
#     django.setup()
#     call_command("makemigrations")
#     call_command("migrate")
#
#     # встановити перемінну оточення
#     set_environment()
#
#     # додати цей файл в PATH
#     sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#
#     # встановити перемінну оточення DJANGO_SETTINGS_MODULE
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
#
#     # ініціалізація DJANGO
#     django.setup()
#
#     # виконання міграцій та запуску сервера
#     call_command("makemigrations")
#     call_command("migrate")
#     IP_ADDRESS = os.environ.get('IP_ADDRESS', '127.0.0.1:8000')
#     call_command("runserver", [IP_ADDRESS, "--noreload"])
#
#
# if __name__ == "__main__":
#     main()
