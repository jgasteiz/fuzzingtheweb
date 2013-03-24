from django.core.management.base import BaseCommand, CommandError
from news.views import update_feed_internal

class Command(BaseCommand):
    help = 'Updates the hacker news feed'

    def handle(self, *args, **options):
        response = str(update_feed_internal())
        self.stdout.write(response)
