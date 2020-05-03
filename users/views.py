from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from playlists.models import Playlist
from .models import Profile
from django.contrib.auth.forms import UserCreationForm



class Detail(DetailView):
	model = User
	def get_object(self, **kwargs):
		return get_object_or_404(User,username=self.kwargs['username'])




def create(req):
	if req.method == 'POST':
		f = UserCreationForm(req.POST)
		if f.is_valid():
			f.save()
		return redirect('playlists-index')
	else:
		userform = UserCreationForm()
	return render(req, 'registration/create.html', {'userform':userform})

@login_required()
def add_pl_to_fav(req,plid):
	if req.method == 'POST':
		pl = Playlist.objects.get(id=plid)
		usr = req.user
		usr.profile.favorites.add(pl)
		usr.save()
	return redirect('playlists-detail', pk=plid)

