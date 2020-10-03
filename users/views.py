from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from playlists.models import Playlist
from .forms import NewUser
# from django.contrib.auth.forms import UserCreationForm
# from .models import Profile


class Detail(DetailView):
	model = User
	def get_object(self, **kwargs):
		return get_object_or_404(User,username=self.kwargs['username'])

def create(req):
	if req.method == 'POST':
		f = NewUser(req.POST)
		if f.is_valid():
			f.save()
		return redirect('playlists-index')
	else:
		userform = NewUser()
	return render(req, 'registration/create.html', {'userform':userform})

@login_required()
def add_pl_to_fav(req,plid):
	if req.method == 'POST':
		pl = get_object_or_404(Playlist,id=plid)
		usr = req.user
		usr.profile.favorites.add(pl)
		usr.save()
	return JsonResponse({'success':'yes'})

@login_required()
def remove_fav(req,plid):
	if req.method == 'POST':
		pl = get_object_or_404(Playlist,id=plid)
		usr = req.user
		usr.profile.favorites.remove(pl)
		usr.save()
	return JsonResponse({'success':'yes'})
