import json
from django.http import JsonResponse
from django.core.serializers import serialize
from playlists.models import Playlist
from comments.models import Comment
from django.contrib.auth.decorators import login_required


# Create your views here.
def playlists_index(req):
    data = serialize('json', Playlist.objects.all(),use_natural_foreign_keys=True)
    return JsonResponse(json.loads(data),safe=False)

def playlists_detail(req,id):
    data = serialize('json', Playlist.objects.filter(pk=id),use_natural_foreign_keys=True)
    return JsonResponse(json.loads(data),safe=False)

def comments_index(req):
    data = serialize('json', Comment.objects.all(),use_natural_foreign_keys=True)
    return JsonResponse(json.loads(data),safe=False)

def comments_in_playlist(req,id):
    data = serialize('json', Comment.objects.filter(playlist=(Playlist.objects.get(pk=id))),use_natural_foreign_keys=True)
    return JsonResponse(json.loads(data),safe=False)

@login_required()
def user_favorite_playlists(req, id):
    user = req.user
    user_favorites = user.profile.favorites.all()
    data = serialize('json', user_favorites, use_natural_foreign_keys=True)
    return JsonResponse(json.loads(data))
