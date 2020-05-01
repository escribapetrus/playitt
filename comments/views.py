import json
from django.http import JsonResponse
from django.shortcuts import render,redirect
from playlists.models import Playlist
from django.contrib.auth.decorators import login_required
from .models import Comment
from .forms import NewComment

# Create your views here.
# @login_required()
# def create(req,id):
#     if req.method == "POST":
#         f = NewComment(req.POST)
#         if f.is_valid():
#             nc = Comment()
#             nc.text=f.cleaned_data['text']
#             nc.user = req.user
#             nc.playlist = Playlist.objects.get(id=id)
#             nc.save()
#     return redirect('playlists-detail', id)


@login_required()
def create(req,id):
    if req.method == "POST":
        f = NewComment(json.loads(req.body.decode('utf-8')))
        if f.is_valid():
            nc = Comment()
            nc.text=f.cleaned_data['text']
            nc.user = req.user
            nc.playlist = Playlist.objects.get(id=id)
            nc.save()
    return JsonResponse({'success': 'yes'})
