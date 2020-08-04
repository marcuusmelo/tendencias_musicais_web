import json
from tendencias_musicais_app.models import SpotifyData
from django.db.models import Max, Min, Avg, F, Count
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

def dashboard(request):
    # Default Country
    # Get requested country, if any. If none, add GLOBAL as default
    if 'country' in request.GET:
        country = request.GET['country']
    else:
        request.GET._mutable = True
        country = 'GLOBAL'
        request.GET['country'] = country

    # Get user info
    username = request.user.username

    # Get playlist general info
    playlist_info_request = playlist_general_info(request)
    playlist_info_data = json.loads(playlist_info_request.content)['data'][0]

    # Get top artists
    top_artists_request = top_10_artists(request)
    top_artists_data = json.loads(top_artists_request.content)['data']

    # Get top musics
    top_musics_request = top_10_musics(request)
    top_musics_data = json.loads(top_musics_request.content)['data']

    context = {
        'username': username,
        'country': country,
        'playlist_info_data': playlist_info_data,
        'top_artistis_data': top_artists_data,
        'top_musics_data': top_musics_data
    }

    return render(request, 'dashboard.html', context=context)


@login_required(login_url='/login')
def home(request):
    """
    View for the home page
    """
    return render(request, 'app_home.html')

@login_required(login_url='/login')
def playlist_general_info(request):
    """
    Informações gerais sobre cada playlist: país, duração max, duração min, duração média.
    """
    spotify_data = SpotifyData.objects.all()

    if 'country' in request.GET:
        country = request.GET['country']
        spotify_data = spotify_data.filter(playlist_id__country__exact=country)

    spotify_data = spotify_data.values('playlist_id_id').annotate(
        duration_max=Max('duration'),
        duration_min=Min('duration'),
        duration_avg=Avg('duration'),
        country=F('playlist_id__country')
    )

    spotify_data_response = list(spotify_data)

    return JsonResponse({'data': spotify_data_response})

@login_required(login_url='/login')
def top_10_artists(request):
    """
    Top 10 artistas: 10 artistas com mais aparições pelas playlists ou em melhor posição nos rankings
    """
    spotify_data = SpotifyData.objects.all()

    if 'country' in request.GET:
        country = request.GET['country']
        spotify_data = spotify_data.filter(playlist_id__country__exact=country)

    spotify_data = spotify_data.values('main_artist_id_id').annotate(
        artist_count=Count('main_artist_id_id'),
        artis_name=F('main_artist_id__name')
    )

    spotify_data = spotify_data.order_by('-artist_count')

    spotify_data_response = list(spotify_data)[:10]

    return JsonResponse({'data': spotify_data_response})

@login_required(login_url='/login')
def top_10_musics(request):
    """
    """
    spotify_data = SpotifyData.objects.all()

    country = None
    if 'country' in request.GET:
        country = request.GET['country']
        spotify_data = spotify_data.filter(playlist_id__country__exact=country)

    spotify_data = spotify_data.values('song_name').annotate(
        song_count=Count('song_name'),
        avg_popularity=Avg('popularity')
    )

    spotify_data = spotify_data.order_by(*['-song_count', '-popularity'])

    spotify_data_response = list(spotify_data)[:10]

    return JsonResponse(
        {
            'data': spotify_data_response,
            'country': country
        }
    )

@login_required(login_url='/login')
def music_influence(request, country_a, country_b):
    """
    Influência musical entre as playlists
    """
    print(country_a)
    print(country_b)
    return JsonResponse({'Test': 'music_influence'})
