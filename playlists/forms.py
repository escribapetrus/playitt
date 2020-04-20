from django import forms

class NewPlaylist(forms.Form):
    title = forms.CharField(
        label="create your playlist", 
        max_length=120,  widget= forms.TextInput(
            attrs={'placeholder':'Your amazing playlist'}
        )
    )

class AddSong(forms.Form):
    title = forms.CharField(label="Title", max_length=120)
    artist = forms.CharField(label="Artist", max_length=120)
    album = forms.CharField(label="Album", max_length=120)

class AddGenre(forms.Form):
    name = forms.CharField(label="Name", max_length=120)
