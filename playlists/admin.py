from django.contrib import admin
from .models import Artist, Song, Album, Playlist,Genre
# Register your models here.
admin.site.register([Artist,Song,Album,Genre, Playlist])
