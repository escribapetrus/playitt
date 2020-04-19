from django.urls import path
from . import views

urlpatterns = [
    path('',views.PlaylistIndex.as_view(), name='playlists-index'),    
    path('detail/<int:pk>/', views.PlaylistDetail.as_view(), name='playlists-detail'),
    path('create/',views.PlaylistCreate.as_view(), name='playlists-create'),
    path('update/<int:pk>/', views.PlaylistUpdate.as_view(), name='playlists-update'),
    path('delete/<int:pk>/', views.PlaylistDelete.as_view(), name='playlists-delete'),

    path('genre/<str:name>/',views.GenreList.as_view(),name='genre-list'),


    path('addsong/<int:pk>/', views.add_song_to_pl, name='playlists-addsong'),
]