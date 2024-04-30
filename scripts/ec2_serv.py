from django.core.management import call_command
from postgres_migration import postgres_migration


def run_prod_server():
    # виконати міграції
    postgres_migration()
    # запустити сервер
    call_command("runserver", ["0.0.0.0:8000", "--noreload"])
