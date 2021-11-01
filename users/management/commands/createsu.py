from django.core.management.base import BaseCommand
from users.models import User

""" 일반 유저가 아닌 superuser 생성하고 싶음"""


class Command(BaseCommand):
    help = "This command creates superuser"

    def handle(self, *args, **options):
        admin = User.objects.get_or_none(username="ebadmin")
        if not admin:
            User.objects.create_superuser("ebadmin", "hhs@hongsub95.co", "1234")
            self.stdout.write(self.style.SUCCESS("Superuser Created"))
        else:
            self.stdout.write(self.style.SUCCESS("Superuser Exists"))