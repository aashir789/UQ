from django.db import models

class Group(models.Model):
    group_name = models.CharField(max_length=50)
    group_pw = models.CharField(max_length=50)

class Song(models.Model):
    song_name = models.CharField(max_length=50)
    song_url = models.CharField(max_length=50)
    song_score = models.IntegerField(blank=True, null=True)
    song_group = models.ForeignKey(Group, blank=True, null=True)
    def __unicode__(self):
        return self.song_url

