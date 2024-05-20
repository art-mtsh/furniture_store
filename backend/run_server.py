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
        os.environ['IP_ADDRESS'] = '127.0.0.1:443'
    else:
        os.environ['ENVIRONMENT'] = 'production'
        os.environ['IP_ADDRESS'] = '0.0.0.0:443'


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

    IP_ADDRESS = os.environ.get('IP_ADDRESS', '127.0.0.1:443')
    call_command("runserver", [IP_ADDRESS, "--noreload"])
    call_command("runserver", [IP_ADDRESS, "--cert dev_ssl.crt --key dev_ssl.key"])


if __name__ == "__main__":
    main()
