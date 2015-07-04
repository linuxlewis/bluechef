class RecipeParser(object):

    def __init__(self, html):
        self.html = html

    @property
    def name(self):
        """
        Returns a str of the recipe name
        """
        return self.html.findtext('.//h1').replace('\n', '') + ' ' \
            + self.html.findtext('.//h2').replace('\n', '')

    @property
    def ingredients(self):
        """
        Returns a list of ingredients

        ['1 pound of ground beef',
        'lots of veggies', ...]
        """
        return list(map(lambda x: x.text_content().replace('\n', ''),
                        self.html.xpath("//ul[@class = 'ingredients-list']/li")))

    @property
    def steps(self):
        """
        Returns a dictionary of the steps of the recipe

        {'recipe':
            {'1':
                'title': 'Section title',
                'steps': ['This is the first sentence',
                          'This is the second sentence',
                          ],
             '2':
                'title': 'Section title',
                'steps': ['This is the first', ...]
            }
        }
        """
        recipe = {}
        # get the recipe step blocks
        steps = list(
            self.html.xpath("//div[@class='instr-wrap' and count(div)=2]"))
        # take only the first half (there are duplicates)
        for i in range(0, int(len(steps) / 2)):
            element = steps[i]
            headers = element.xpath('div/span/text()')
            steps_p = element.xpath("div[@class='instr-txt']")
            # split the number key and section title
            recipe[headers[0]] = {'title': headers[1].replace('\n', '')[:-1].strip(),
                                  'steps': [x.strip() for x in steps_p[0].text_content().replace('\n', '').split('.') if x]}
        return recipe
