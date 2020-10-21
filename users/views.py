from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from playlists.models import Playlist
from .forms import NewUser


class Detail(DetailView):
	model = User
	def get_object(self, **kwargs):
		return get_object_or_404(User,username=self.kwargs['username'])

def create(req):
	if req.method == 'POST':
		userform = NewUser(req.POST)
		if userform.is_valid():
			new_user = userform.save()
			new_user = authenticate(username=userform.cleaned_data['username'], password=userform.cleaned_data['password1'])
			login(req, new_user)
			return redirect('users-auth-redirect')
	else:
		userform = NewUser()
	return render(req, 'registration/create.html', {'userform':userform})

def auth_redirect(req):
	username = req.user
	return render(req, "registration/auth_redirect.html", {'username': username})

@login_required()
def add_pl_to_fav(req,plid):
	if req.method == 'POST':
		pl = get_object_or_404(Playlist,id=plid)
		usr = req.user
		usr.profile.favorites.add(pl)
		usr.save()
	return JsonResponse({'success': True})

@login_required()
def remove_fav(req,plid):
	if req.method == 'POST':
		pl = get_object_or_404(Playlist,id=plid)
		usr = req.user
		usr.profile.favorites.remove(pl)
		usr.save()
	return JsonResponse({'success':True})
