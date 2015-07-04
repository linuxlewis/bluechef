# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20150626_0718'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='data',
            new_name='steps',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=2048), default=[], size=None),
            preserve_default=False,
        ),
    ]
