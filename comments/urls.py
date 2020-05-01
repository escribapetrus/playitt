from django.urls import path
from . import views

urlpatterns = [
    path('playlists/<int:id>/', views.create, name='comments-create'),
]