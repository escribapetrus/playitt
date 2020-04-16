from django.shortcuts import render,redirect
from playlists.models import Playlist
from .models import Comment
from .forms import NewComment

# Create your views here.
def create(req,id):
    if req.method == "POST":
        f = NewComment(req.POST)
        if f.is_valid():
            nc = Comment()
            nc.text=f.cleaned_data['text']
            nc.user = req.user
            nc.playlist = Playlist.objects.get(id=id)
            nc.save()
            return redirect('playlists-detail', id)


