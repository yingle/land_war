# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_auto_20160726_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='votes',
            field=models.FloatField(default=50.0),
        ),
    ]
