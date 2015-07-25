# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UQ', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('song_name', models.CharField(max_length=50)),
                ('song_url', models.CharField(max_length=50)),
                ('song_rank', models.CharField(max_length=50)),
                ('song_group_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='group',
            old_name='group_id',
            new_name='group_pw',
        ),
    ]
