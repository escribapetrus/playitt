from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from playlists.models import Playlist

# Create your views here.
def create(req):
	if req.method == 'POST':
		f = UserCreationForm(req.POST)
		if f.is_valid():
			f.save()
		return redirect('playlists-index')
	else:
		userform = UserCreationForm()
	return render(req, 'registration/create.html', {'userform':userform})

def profile(req):
	return render(req,'registration/profile.html')

def add_pl_to_fav(req,plid):
	if req.method == 'POST':
		pl = Playlist.objects.get(id=plid)
		usr = req.user
		usr.profile.favorites.add(pl)
		usr.save()
		return redirect('playlists-detail', id=plid)
