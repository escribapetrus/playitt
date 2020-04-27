from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('playlists.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('comments/', include('comments.urls')),
    path('api/', include('api.urls')),
]
