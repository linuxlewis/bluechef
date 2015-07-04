import os

from lxml import html
from django.test import TestCase

from recipes import parser

script_dir = os.path.dirname(__file__)
recipe_fixture_path = os.path.join(script_dir, 'recipe.html')


class TestRecipeParser(TestCase):

    maxDiff = None

    def setUp(self):
        self.parser = parser.RecipeParser(
            html.parse(
                open(
                    recipe_fixture_path,
                    'rb')))

    def test_name(self):
        self.assertEqual(
            self.parser.name,
            "Lamb & Risotto-Style Ditalini Pasta with Spring Onion & Green Beans")

    def test_ingredients(self):
        ingredients = ['7 Ounces Ground Lamb & Beef Blend',
                       '5 Ounces Ditalini Pasta',
                       '6 Ounces Green Beans',
                       '3 Cloves Garlic',
                       '1 Spring Onion',
                       '1 Lemon',
                       '1 Bunch Mint',
                       '1 Tablespoon Butter',
                       '\xbc Cup Grated Parmesan Cheese']
        self.assertEqual(self.parser.ingredients, ingredients)

    def test_steps(self):

        data = {
            '1': {'steps':
                  ['Wash and dry the fresh produce',
                   'Trim off and discard the stem ends of the green beans; '
                   'cut the green beans into \xbd-inch pieces',
                   'Peel and mince the garlic',
                   'Cut off and discard the root end of the spring onion',
                   'Thinly slice the green top of the spring onion on an '
                   'angle; halve and thinly slice the white bottom',
                   'Using a peeler, remove the rind of the lemon, avoiding '
                   'the pith; mince the rind to get 2 teaspoons of '
                   'zest\u200b (or use a zester)',
                   'Quarter and deseed the lemon',
                   'Pick the mint leaves off the stems; discard the stems '
                   'and finely chop the leaves'],
                  'title': 'Prepare the ingredients'},
            '2': {'steps': ['In a large pan, heat 2 teaspoons of olive oil on '
                            'medium-high until hot',
                            'Add the ground lamb and beef blend; season with salt '
                            'and pepper',
                            'Cook, frequently breaking the meat apart with a spoon, '
                            '3 to 5 minutes, or until browned and cooked through'],
                  'title': 'Cook the meat'},
            '3': {'steps': ['Reduce the heat to medium and add the garlic and white '
                            'bottom of the spring onion to the pan; season with salt '
                            'and pepper',
                            'Cook, stirring occasionally, 2 to 4 minutes, or until '
                            'the aromatics are lightly browned and fragrant'],
                  'title': 'Add the aromatics'},
            '4': {'steps': ['Add the pasta, lemon zest and 2 \xbd cups of water to the '
                            'pan; season with salt and pepper',
                            'Cook, stirring frequently, 10 to 12 minutes, or until '
                            'the pasta is al dente (still slightly firm to the bite)'],
                  'title': 'Add the pasta'},
            '5': {'steps': ['Add the green beans to the pan; season with salt and '
                            'pepper',
                            'Cook, stirring frequently, 1 to 2 minutes, or until the '
                            'green beans are bright green and slightly softened',
                            'Season with salt and pepper and remove from heat'],
                  'title': 'Add the green beans'},
            '6': {'steps': ['Add the Parmesan cheese, butter, the juice of 2 lemon '
                            'wedges and 2 tablespoons of water to the pan',
                            'Stir until thoroughly combined and season with salt and '
                            'pepper to taste',
                            'Divide the finished pasta between 2 dishes',
                            'Garnish with the mint, green top of the spring onion '
                            'and remaining lemon wedges',
                            'Enjoy!'],
                  'title': 'Finish & plate your dish'}}

        self.assertEqual(self.parser.steps, data)
