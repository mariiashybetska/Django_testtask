from django.core.management.base import BaseCommand
from django.apps import apps

'''
commands - create django command that prints all models and object counts.
'''


class Command(BaseCommand):
    help = 'Return info about all models and count its objects'

    def handle(self, *args, **options):
        models = apps.get_models()
        for model in models:
            print(f'Model:{model}, Count Objects {model.objects.all().count()}')
