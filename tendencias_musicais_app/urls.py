from django.urls import path, re_path
from tendencias_musicais_app.views import home, playlist_general_info, top_10_artists, \
    top_10_musics, music_influence

app = 'tendencias_musicais_app'

urlpatterns = [
    path('', home, name='homepage'),
    path('playlist_info/', playlist_general_info, name='playlist_info'),
    path('top_10_artists/', top_10_artists, name='top_10_artists'),
    path('top_10_musics/', top_10_musics, name='top_10_musics'),
    # re_path(r'^music_influence/(?P<country_a>[A-Z])/(?P<country_b>[A-Z])/$', music_influence, name='music_influence'),
    path('music_influence/<str:country_a>/<str:country_b>/', music_influence, name='music_influence'),
]
