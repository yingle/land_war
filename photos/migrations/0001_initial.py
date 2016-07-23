# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filename', models.CharField(max_length=100)),
                ('kind', models.CharField(max_length=50)),
                ('upload_data', models.DateTimeField(verbose_name=b'date of upload')),
                ('description', models.CharField(max_length=300)),
                ('match_number', models.IntegerField(default=0)),
                ('votes', models.IntegerField(default=50)),
                ('city', models.CharField(max_length=30)),
                ('createUser', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
