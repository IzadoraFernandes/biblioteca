from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create groups"

    def handle(self, *args, **options):
        groups = ["Bibliotecarios", "Usuarios"]
        group_count_in_database = Group.objects.all().count()

        if group_count_in_database == len(groups):
            message = "Groups: already runned"
            self.stdout.write(self.style.WARNING(message))
        else:
            [Group.objects.get_or_create(name=group) for group in groups]
            self.stdout.write(self.style.SUCCESS("Groups: successfully created"))