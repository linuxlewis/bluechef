import requests
from lxml import html
from django.core.management.base import BaseCommand

from recipes import parser, models


class Command(BaseCommand):
    help = 'Scrapes BlueApron and saves the recipe data'

    BASE_URL = 'https://www.blueapron.com/recipes/{}'

    def add_arguments(self, parser):

        parser.add_argument('--index',
                            action='store',
                            dest='index',
                            type=int,
                            default=1,
                            help='Start recipe search by the given index')

    def handle(self, *args, **options):

        for external_id in range(options['index'], 1000):

            url = self.BASE_URL.format(external_id)
            self.stdout.write('requesting {}'.format(url))

            r = requests.get(url)

            if r.status_code == 200:
                h = html.fromstring(r.text)
                self.create_recipe(h, external_id)
            else:
                self.stdout.write('url: {} failed status:{}'.format(url, str(r.status_code)))

        self.stdout.write('import complete')

    def create_recipe(self, ht, external_id):
        p = parser.RecipeParser(ht)
        try:
            recipe = models.Recipe.objects.get(external_id=external_id)
        except models.Recipe.DoesNotExist:
            recipe = models.Recipe(external_id=external_id)
        recipe.name = p.name
        recipe.ingredients = p.ingredients
        recipe.steps = p.steps
        recipe.save()

        return recipe
