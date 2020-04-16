from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect

urlpatterns = [
    path('', include('playlists.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls'))
]
