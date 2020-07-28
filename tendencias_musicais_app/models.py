from django.db import models

# Create your models here.
class Playlists(models.Model):
    playlist_id = models.CharField(max_length=126, primary_key=True)
    name = models.CharField(max_length=126)
    country = models.CharField(max_length=126)
    source = models.CharField(max_length=126)


class Artists(models.Model):
    artist_id = models.CharField(max_length=126, primary_key=True)
    name = models.CharField(max_length=126)
    music_genre_1 = models.CharField(max_length=126, null=True, blank=True)
    music_genre_2 = models.CharField(max_length=126, null=True, blank=True)
    music_genre_3 = models.CharField(max_length=126, null=True, blank=True)


class SpotifyData(models.Model):
    playlist_id = models.ForeignKey('Playlists', on_delete=models.PROTECT)
    main_artist_id = models.ForeignKey('Artists', on_delete=models.PROTECT)
    all_artists = models.CharField(max_length=255)
    all_artists_ids = models.CharField(max_length=255)
    release_date = models.DateField()
    duration = models.IntegerField()
    song_name = models.CharField(max_length=126)
    popularity = models.IntegerField()
    position = models.IntegerField()
    source_date = models.DateTimeField()
