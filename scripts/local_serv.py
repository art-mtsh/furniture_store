from django.core.management import call_command
from sqlite_migration import sqlite_migration


def run_local_server():
    # виконати міграції
    sqlite_migration()
    # запустити сервер
    call_command("runserver", ["127.0.0.1:8000", "--noreload"])
