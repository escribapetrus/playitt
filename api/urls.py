from django.urls import path
from . import views

urlpatterns = [
    path('playlists/',views.playlists_index, name='api-playlists-index'),
    path('playlists/<int:id>/',views.playlists_detail, name='api-playlists-detail'),
    path('playlists/user-favorites',views.playlists_index, name='api-user-favorites'),
    path('comments/',views.comments_index,name='api-comments-index'),
    path('comments/playlists/<int:id>/',views.comments_in_playlist,name='api-comments-playlist'),
]