from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def create(req):
	if req.method == 'POST':
		f = UserCreationForm(req.POST)
		if f.is_valid():
			f.save()
		return HttpResponseRedirect('/playlists')
	else:
		user = req.user
		userform = UserCreationForm()
		return render(req, 'registration/create.html', {'user': user,'userform':userform})
