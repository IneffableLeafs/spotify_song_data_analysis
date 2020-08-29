import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

scope = 'user-library-read'
os.environ["SPOTIPY_REDIRECT_URI"] = "http://127.0.0.1:9090"
os.environ["SPOTIPY_CACHE_PATH"] = "/Users/peter/spotipy-cache"



sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="43dfe303cbce478e8c8952eed351e881",
                                               client_secret="3b8aa6ee50b64d9bb16ba09554b0b51e",
                                               redirect_uri="http://127.0.0.1:9090",
                                               username="ineffableleaves",
                                               scope="user-library-read"))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])