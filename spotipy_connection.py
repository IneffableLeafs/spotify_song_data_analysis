import spotipy
from spotipy.oauth2 import SpotifyOAuth

# type your client_id, client_secret, and username (put them between quotation marks):
client_id = "-----------------------"
client_secret = "----------------------"
username = "------------------"


scope = 'user-library-read user-read-recently-played playlist-modify-private playlist-read-private'
redirect_uri = "http://localhost:8888/callback"

# authenticate and connect spotipy to spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               username=username,
                                               scope=scope))