from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth.models import User
from .models import Playlist, Artist, Album, Song
from .forms import NewPlaylist, AddSong

def index(req): 
    f = NewPlaylist()
    pl = Playlist.objects
    return render(req,'playlists/index.html', {'user': req.user,'pl':pl.all,'display':pl.latest('id'), 'form':f})

def detail(req,id):
    pl = Playlist.objects.get(pk=id)
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
            return HttpResponseRedirect('/playlists')
        else:
            HttpResponseRedirect("/playlists")
    else:
        songs = pl.songs.all()
        f = AddSong()
        return render(req,'playlists/detail.html',{'user': req.user,'pl':pl,'songs':songs,'form':f})

def create(req):
    if req.method == 'POST':
        f = NewPlaylist(req.POST)
        if f.is_valid():
            try:
                # usr = User.objects.get(username=req.user)
                np = Playlist(title=f.cleaned_data['title'])
                np.user_id = req.user
                np.save()
                return HttpResponseRedirect('/playlists/detail/{}'.format(np.pk))
            except:
                return HttpResponseRedirect('/users/login')
    else:
        f = NewPlaylist()
        return render(req, 'playlists/create.html', {'user': req.user,'form': f})