from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile

class NewUser(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['username'].widget.attrs['placeholder'] = 'Username'
        # self.fields['email'].widget.attrs['placeholder'] = 'Email'
        # self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        # self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        # self.fields['username'].widget.attrs.pop("autofocus", None)

        self.fields['username'].label = "Username"
        self.fields['email'].label = "Email"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm password"

    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        # widgets = {
        #     'username': forms.fields.TextInput(attrs={'placeholder': 'adamsandlerfan2006'}),
        #     'email': forms.fields.TextInput(attrs={'sandmanfan2006@gmail.com'})
        # }

class AddFavorites(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['favorites']
