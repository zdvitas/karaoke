
from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Song(models.Model):
    number = models.IntegerField()
    tittle = models.CharField(max_length=50)
    minus_quality = models.CharField(max_length=30)
    back_vocal = models.CharField(max_length=30)
    karaoke_system = models.CharField(max_length=30)
    artist = models.ForeignKey(Artist)


class Line(models.Model):
    song = models.ForeignKey(Song)
    table = models.IntegerField()
    date = models.DateTimeField()


class NowPlay(models.Model):
    song = models.ForeignKey(Song)
    table = models.IntegerField()
