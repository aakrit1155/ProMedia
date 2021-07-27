from django.contrib.auth.models import User
from django import forms
from .models import Song, Album


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['song_title', 'audio_file','lyrics']


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['artist', 'album_title', 'genre', 'album_logo']
