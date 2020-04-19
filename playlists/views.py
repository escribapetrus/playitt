from django.shortcuts import render,redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Playlist, Artist, Album, Song
from .forms import NewPlaylist, AddSong
from comments.forms import NewComment

class Index(ListView):
    model = Playlist
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = NewPlaylist()
        return context

class Detail(DetailView):
    model = Playlist
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = NewComment()
        context['song_form'] = AddSong()
        return context

class Create(LoginRequiredMixin, CreateView):
    model = Playlist
    fields = ['title','description']
    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)

class Update(UpdateView):
    model = Playlist
    fields = ['title','songs','description']
    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)

class Delete(DeleteView):
    model = Playlist
    success_url = '/'
    def test_func(self):
        pl = self.get_object()
        if pl.user_id == self.request.user:
            return True
        else:
            return False

def add_song_to_pl(req,pk):
    pl = Playlist.objects.get(pk=pk)
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
            return redirect('playlists-detail', pk)
