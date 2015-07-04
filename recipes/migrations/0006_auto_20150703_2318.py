# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_auto_20150703_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='external_id',
            field=models.CharField(max_length=1024, unique=True, blank=True),
        ),
    ]
