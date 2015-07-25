# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UQ', '0002_auto_20150725_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songs',
            name='song_group_id',
        ),
        migrations.RemoveField(
            model_name='songs',
            name='song_rank',
        ),
    ]
