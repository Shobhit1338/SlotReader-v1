from django.core.management.base import BaseCommand, CommandError
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = "Check database connectivity for the default connection."

    def handle(self, *args, **options):
        connection = connections["default"]
        try:
            connection.ensure_connection()
        except OperationalError as exc:
            raise CommandError(f"Database connection failed: {exc}") from exc
        self.stdout.write(self.style.SUCCESS("Database connection successful."))
