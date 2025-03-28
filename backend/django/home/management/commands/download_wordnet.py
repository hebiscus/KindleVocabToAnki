import nltk

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Downloads wordnet nltk dictionary database"

    def handle(self, *args, **options):
        nltk.download("wordnet")
        self.stdout.write(self.style.SUCCESS("Successfully downloaded wordnet"))
