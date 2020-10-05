from django.urls import path
from . import views

urlpatterns = [
	path('create/', views.create, name='users-create'),
	path('detail/<str:username>/',views.Detail.as_view(),name='users-profile'),
	path('add-to-fav/playlists/<int:plid>/',views.add_pl_to_fav, name='users-addtofav'),
	path('remove-fav/playlists/<int:plid>/',views.remove_fav, name='users-removefav'),
	path('auth-redirect',views.auth_redirect, name='users-auth-redirect')
]