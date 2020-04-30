from django.urls import path
from . import views

urlpatterns = [
    path('playlists/',views.playlists_index, name='api-playlists-index'),
    path('playlists/<int:id>/',views.playlists_detail, name='api-playlists-detail'),
]