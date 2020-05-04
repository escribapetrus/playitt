from django.urls import path
from . import views

urlpatterns = [
    path('',views.PlaylistIndex.as_view(), name='playlists-index'),    
    path('playlists/<int:pk>/', views.PlaylistDetail.as_view(), name='playlists-detail'),
    path('playlists/create/',views.PlaylistCreate.as_view(), name='playlists-create'),
    path('playlists/<int:pk>/update/', views.PlaylistUpdate.as_view(), name='playlists-update'),
    path('playlists/<int:pk>/delete/', views.PlaylistDelete.as_view(), name='playlists-delete'),
    path('playlists/genre/<str:name>/',views.GenreList.as_view(),name='playlists-genre-list'),
    path('playlists/user/<str:username>/',views.UserList.as_view(),name='playlists-user-list'),
    path('playlists/<int:pk>/removesong/<int:songid>', views.remove_song_in_pl, name='playlists-removesong'),
   	path('playlists/<int:pk>/addsong/', views.add_song_to_pl, name='playlists-addsong'),
   	path('playlists/addgenre',views.add_genre,name='playlists-addgenre')
]