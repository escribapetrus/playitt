import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from comments.forms import NewComment
from .forms import AddGenre, AddSong, NewPlaylist
from .lastfm import search_song
from .models import Album, Artist, Genre, Playlist, Song

class PlaylistIndex(ListView):
    model = Playlist
    queryset = Playlist.objects.order_by('-date_created')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = NewPlaylist()
        context['genres'] = Genre.objects.all()
        return context

class PlaylistDetail(DetailView):
    model = Playlist
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = NewComment()
        context['song_form'] = AddSong()
        return context

class PlaylistCreate(LoginRequiredMixin, CreateView):
    model = Playlist
    fields = ['title','genres','description',]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genre_form'] = AddGenre()
        return context
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PlaylistUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Playlist
    fields = ['title','description','genres']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def test_func(self):
        pl = self.get_object()
        if pl.user == self.request.user:
            return True
        else:
            return False

class PlaylistDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Playlist
    success_url = '/'
    def test_func(self):
        pl = self.get_object()
        if pl.user == self.request.user:
            return True
        else:
            return False

class GenreList(ListView):
    model = Playlist
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = NewPlaylist()
        context['genres'] = Genre.objects.all()
        return context
    def get_queryset(self):
        self.genre = get_object_or_404(Genre, name=self.kwargs['name'])
        glist = Genre.objects.get(name=self.genre).playlist_set.all()
        if glist:
            return Genre.objects.get(name=self.genre).playlist_set.all()
        else:
            return Playlist.objects.all()

class UserList(ListView):
    model = Playlist
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = NewPlaylist()
        context['genres'] = Genre.objects.all()
        return context
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        qlist = Playlist.objects.filter(user=user).order_by('-date_created')
        if qlist:
            return qlist
        else:
            return Playlist.objects.all()


@login_required()
def add_song_to_pl(req,pk):
    pl = Playlist.objects.get(pk=pk)
    if req.method == "POST":
        f = AddSong(json.loads(req.body.decode('utf-8')))
        # f = AddSong(req.POST)
        if f.is_valid() and req.user == pl.user:
            (jackie, jenny) = (f.cleaned_data['artist'],f.cleaned_data['title'])
            try:
                track_info = search_song('track.getInfo',jackie,jenny).json()['track']
                (artist,album,title) = (track_info['artist']['name'],track_info['album']['title'],track_info['name'],)
                try:
                    ar = Artist.objects.get(name=artist)
                except:
                    ar = Artist(name=artist)
                    ar.save()
                try:
                    al = Album.objects.get(title=album)
                except:
                    al = Album(title=album,artist=ar)
                    al.save()
                try:
                    son = Song.Objects.get(title=title)
                except:
                    son = Song(title=title,artist=ar,album=al)
                    son.save()
                finally:
                    pl.songs.add(son)
                    pl.save()
            except:
                return JsonResponse({'message': "track not found"})
        return JsonResponse({'success': 'yes'})

# @login_required()
# def add_song_to_pl(req,pk):
#     pl = Playlist.objects.get(pk=pk)
#     if req.method == "POST":
#         f = AddSong(json.loads(req.body.decode('utf-8')))
#         if f.is_valid():
#             if req.user == pl.user:
#                 (artist, album, title) = (f.cleaned_data['artist'], f.cleaned_data['album'],f.cleaned_data['title'])
#                 try:
#                     ar = Artist.objects.get(name=artist)
#                 except:
#                     ar = Artist(name=artist)
#                     ar.save()
#                 try:
#                     al = Album.objects.get(title=album)
#                 except:
#                     al = Album(title=album,artist=ar)
#                     al.save()
#                 try:
#                     son = Song.Objects.get(title=title)
#                 except:
#                     son = Song(title=title,artist=ar,album=al)
#                     son.save()
#                 finally:
#                     pl.songs.add(son)
#                     pl.save()
#         return JsonResponse({'success': 'yes'})

@login_required()
def remove_song_in_pl(req,pk,songid):
    if req.method == "POST":
        pl = Playlist.objects.get(pk=pk)
        son = Song.objects.get(pk=songid)
        if req.user == pl.user:
            pl.songs.remove(son)
            pl.save()
    return JsonResponse({'success': 'yes'})

@login_required()
def add_genre(req):
    if req.method == "POST":
        genre = AddGenre(req.POST)
        if genre.is_valid():
            g = Genre(name=genre.cleaned_data['name'])
            g.save()
    return redirect('playlists-create')
