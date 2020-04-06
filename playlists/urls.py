from django.urls import path
from . import views

urlpatterns = [
    #index
    path('',views.index, name='index'),    
    #detail
    path('detail/<int:id>', views.detail, name='detail'),
    #new playlist + add songs
    path('create',views.create, name='create')
]