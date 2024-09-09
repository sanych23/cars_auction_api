from django.core.management.base import BaseCommand
from seeds.management.main import Main

class Command(BaseCommand):

    def handle(self, *args, **options):
        Main().start()