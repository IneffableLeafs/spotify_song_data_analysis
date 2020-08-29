# import os
#from spotify_client2 import SpotifyClient

#print("Test")
#spotify_client = SpotifyClient()
#track_info = spotify_client.get_song()
#print(track_info)

import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

os.environ["SPOTIPY_CLIENT_ID"] = "43dfe303cbce478e8c8952eed351e881"
os.environ["SPOTIPY_CLIENT_SECRET"] = "3b8aa6ee50b64d9bb16ba09554b0b51e"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://127.0.0.1:9090"
os.environ["SPOTIPY_CACHE_PATH"] = "/Users/peter/spotipy-cache"

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])