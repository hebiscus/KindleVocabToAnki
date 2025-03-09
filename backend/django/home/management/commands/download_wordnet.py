from django.core.management.base import BaseCommand
import nltk

class Command(BaseCommand):
    help = "Downloads wordnet nltk dictionary database"

    def handle(self, *args, **options):
        def handle(self, *args, **kwargs):
          nltk.download('wordnet')
          self.stdout.write(self.style.SUCCESS('Successfully downloaded wordnet'))

