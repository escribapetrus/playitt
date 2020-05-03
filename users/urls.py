from django.urls import path
from . import views

urlpatterns = [
	path('create/', views.create, name='users-create'),
	path('detail/<str:username>/',views.Detail.as_view(),name='users-profile'),
	path('add-to-fav/<int:plid>/',views.add_pl_to_fav, name='users-addtofav')
]