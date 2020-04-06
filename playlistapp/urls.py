from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect

urlpatterns = [
    path('', lambda req: HttpResponseRedirect('/playlists'), name='home'),  
    path('admin/', admin.site.urls),
    path('playlists/', include('playlists.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls'))
]
