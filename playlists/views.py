from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Playlist, Artist, Album, Song
from .forms import NewPlaylist, AddSong
from comments.forms import NewComment

def index(req): 
    f = NewPlaylist()
    pl = Playlist.objects
    return render(req,'playlists/index.html', {'pl':pl, 'form':f})

def detail(req,id):
    pl = Playlist.objects.get(id=id)
    if req.method == "POST":
        f = AddSong(req.POST)
        if f.is_valid():
            if req.user == pl.user_id:
                (artist, album, title) = (f.cleaned_data['artist'], f.cleaned_data['album'],f.cleaned_data['title'])
                try:
                    ar = Artist.objects.get(name=artist)
                except:
                    ar = Artist(name=artist)
                    ar.save()
                try:
                    al = Album.objects.get(title=album)
                except:
                    al = Album(title=album,artist_id=ar)
                    al.save()
                try:
                    son = Song.Objects.get(title=title)
                except:
                    son = Song(title=title,artist_id=ar,album_id=al)
                    son.save()
                finally:
                    pl.songs.add(son)
                    pl.save()
            return redirect('playlists-detail', id=id)
    else:
        songs = pl.songs.all()
        comments = pl.comment_set.all()
        f = AddSong()
    return render(req,'playlists/detail.html',{'pl':pl,'songs':songs,'comments':comments,'song_form':f,'comment_form': NewComment})

def create(req):
    if req.method == 'POST':
        f = NewPlaylist(req.POST)
        if f.is_valid():
            np = Playlist(title=f.cleaned_data['title'])
            np.user_id = req.user
            np.save()
            return redirect('playlists-detail', id=np.id)
    else:
        f = NewPlaylist()
    return render(req, 'playlists/create.html', {'form': f})