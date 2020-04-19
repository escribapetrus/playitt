from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index.as_view(), name='playlists-index'),    
    path('detail/<int:pk>/', views.Detail.as_view(), name='playlists-detail'),
    path('create/',views.Create.as_view(), name='playlists-create'),
    path('update/<int:pk>/', views.Update.as_view(), name='playlists-update'),
    path('delete/<int:pk>/', views.Delete.as_view(), name='playlists-delete'),
    path('addsong/<int:pk>/', views.add_song_to_pl, name='playlists-addsong'),
]