from django.urls import path
from . import views

urlpatterns = [
	path('create/', views.create, name='users-create'),
	path('profile/',views.profile,name='users-profile'),
	path('add-to-fav/<int:plid>/',views.add_pl_to_fav, name='users-addtofav')
]