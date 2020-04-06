from django import forms

class NewPlaylist(forms.Form):
    title = forms.CharField(label="playlist title", max_length=120)

class AddSong(forms.Form):
    title = forms.CharField(label="Title", max_length=120)
    artist = forms.CharField(label="Artist", max_length=120)
    album = forms.CharField(label="Album", max_length=120)