import os
import sys
import django
import platform
from django.core.management import call_command


def set_environment():
    """
    Визначаємо де ми знаходимось
    :return: "development" or "production"
    """

    if platform.node() == "DESKTOP-5PMV5U1":
        os.environ['ENVIRONMENT'] = 'development'
    else:
        os.environ['ENVIRONMENT'] = 'production'


def main():
    # встановити перемінну оточення
    set_environment()

    # додати цей файл в PATH
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

    # встановити перемінну оточення DJANGO_SETTINGS_MODULE
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

    # ініціалізація DJANGO
    django.setup()

    # виконання міграцій та запуску сервера
    call_command("makemigrations")
    call_command("migrate")
    call_command("runserver", ["0.0.0.0:8000", "--noreload"])


if __name__ == "__main__":
    main()
