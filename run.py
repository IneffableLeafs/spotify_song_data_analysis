import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotify_client import get_song

# prompt user for username
username = input("Enter your Spotify username: ")

scope = 'user-library-read'

# authenticate and connect spotipy to spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="43dfe303cbce478e8c8952eed351e881",
                                               client_secret="3b8aa6ee50b64d9bb16ba09554b0b51e",
                                               redirect_uri="http://127.0.0.1:9090",
                                               username=username,
                                               scope="user-library-read"))

# set the track limit to the max
limit = 50
# set the offset initially to zero
offset = 0

get_song(sp)



