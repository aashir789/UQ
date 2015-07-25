# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UQ', '0004_songs_song_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='song_score',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
