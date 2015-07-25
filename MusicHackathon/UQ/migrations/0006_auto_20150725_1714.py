# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UQ', '0005_songs_song_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('song_name', models.CharField(max_length=50)),
                ('song_url', models.CharField(max_length=50)),
                ('song_score', models.IntegerField(null=True, blank=True)),
                ('song_group', models.ForeignKey(blank=True, to='UQ.Group', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='songs',
            name='song_group',
        ),
        migrations.DeleteModel(
            name='Songs',
        ),
    ]
