from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='playlists-index'),    
    path('detail/<int:id>/', views.detail, name='playlists-detail'),
    path('create/',views.create, name='playlists-create')
]