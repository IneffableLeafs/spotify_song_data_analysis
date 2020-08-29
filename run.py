import spotipy
from spotipy.oauth2 import SpotifyOAuth

username = input("Enter your Spotify username: ")

scope = 'user-library-read'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="43dfe303cbce478e8c8952eed351e881",
                                               client_secret="3b8aa6ee50b64d9bb16ba09554b0b51e",
                                               redirect_uri="http://127.0.0.1:9090",
                                               username=username,
                                               scope="user-library-read"))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])