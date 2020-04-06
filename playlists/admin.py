from django.contrib import admin
from .models import Artist, Song, Album, Playlist
# Register your models here.
admin.site.register([Artist,Song,Album,Playlist])
