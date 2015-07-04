# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20150627_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='external_id',
            field=models.TextField(blank=True),
        ),
    ]
