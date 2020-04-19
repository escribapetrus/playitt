from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Artist(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=50)
    release_year = models.IntegerField
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=50)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Playlist(models.Model):
    title = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)
    description = models.TextField(default="")
    date_created = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('playlists-detail', kwargs={'pk':self.pk})




