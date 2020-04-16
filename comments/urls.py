from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:id>', views.create, name='comments-create'),
]