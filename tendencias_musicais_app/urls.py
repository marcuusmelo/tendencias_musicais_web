from django.urls import path, re_path
from tendencias_musicais_app.views import home, playlist_general_info, top_10_artists, \
    top_10_musics, music_influence, dashboard

app = 'tendencias_musicais_app'

urlpatterns = [
    path('', home, name='app_homepage'),
    path('playlist_info/', playlist_general_info, name='playlist_info'),
    path('top_10_artists/', top_10_artists, name='top_10_artists'),
    path('top_10_musics/', top_10_musics, name='top_10_musics'),
    path('music_influence/<str:country_a>/<str:country_b>/', music_influence, name='music_influence'),
    path('dashboard/', dashboard, name='dashboard')
]
