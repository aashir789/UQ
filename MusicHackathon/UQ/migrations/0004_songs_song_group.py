# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UQ', '0003_auto_20150725_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='song_group',
            field=models.ForeignKey(blank=True, to='UQ.Group', null=True),
        ),
    ]
