from django.db import models
from django.contrib.auth.models import User
from playlists.models import Playlist
from django.utils import timezone

# Create your models here.
class Comment(models.Model):
    text = models.TextField()
    playlist = models.ForeignKey(Playlist,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment_date = models.DateField(default=timezone.now)
    