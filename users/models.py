from django.db import models
from django.contrib.auth.models import User
from playlists.models import Playlist

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    favorites = models.ManyToManyField(Playlist)
    def __str__(self):
        return self.user.username
