import os
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=os.getenv('SPOTIFY_CLIENT_ID'), client_secret=os.getenv('SPOTIFY_CLIENT_SECRET')))

def find_artist_album_track(artist, song):
    try: 
        res = sp.search(q=f"{artist} {song}", type="track")
        tracks = res["tracks"]["items"]
        tracks_ = list(filter(lambda x: x["album"]["album_type"] == "album", tracks))
        # sorted_tracks = sorted(tracks_, key=lambda track: track["album"]["release_date"])
        return list(map(lambda x: (x["artists"][0]["name"], x["album"]["name"], x["name"]), tracks_))[0]
    except: 
        print("not found")