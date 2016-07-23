# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.ImageField(default=datetime.datetime(2016, 7, 23, 16, 24, 12, 947139, tzinfo=utc), upload_to=b'dir_upload/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='kind',
            field=models.CharField(max_length=50, choices=[(b'BEACH', b'Beach'), (b'MOUNTAIN', b'Mountain'), (b'CASTEL', b'Castel')]),
        ),
    ]
