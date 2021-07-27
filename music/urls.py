from django.contrib import admin
from django.urls import path
from . import views
app_name = 'music'
urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('login_user/', views.login_user, name="login_user"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('<int:album_id>/', views.detail, name="detail"),
    path('<int:song_id>/favorite/', views.favorite, name="favorite"),
    path('songs/<filter_by>/', views.songs, name="songs"),
    path('create_album/', views.create_album, name="create_album"),
    path('<album_id>/create_song/', views.create_song, name="create_song"),
    path('<album_id>/delete_song/<song_id>/', views.delete_song, name="delete_song"),
    path('<album_id>/favorite_album/', views.favorite_album, name="favorite_album"),
    path('<album_id>/delete_album/', views.delete_album, name="delete_album"),
]
