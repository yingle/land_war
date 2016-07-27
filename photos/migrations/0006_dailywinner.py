# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_auto_20160726_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyWinner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('race_date', models.DateField()),
                ('winnerPhoto', models.ForeignKey(to='photos.Photo')),
            ],
        ),
    ]
