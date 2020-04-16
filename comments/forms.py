from django import forms

class NewComment(forms.Form):
    text = forms.CharField(widget=forms.Textarea)