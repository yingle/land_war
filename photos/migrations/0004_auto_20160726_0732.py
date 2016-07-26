# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_remove_photo_filename'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='upload_data',
            new_name='upload_date',
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to=b'dir_upload'),
        ),
    ]
