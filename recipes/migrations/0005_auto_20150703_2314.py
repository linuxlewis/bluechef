# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipe_external_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='steps',
            field=jsonfield.fields.JSONField(),
        ),
    ]
