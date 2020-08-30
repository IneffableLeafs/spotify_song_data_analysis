import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotify_client import SpotifyClient

# prompt user for username
username = input("Enter your Spotify username: ")

scope = 'user-library-read'

# authenticate and connect spotipy to spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="43dfe303cbce478e8c8952eed351e881",
                                               client_secret="3b8aa6ee50b64d9bb16ba09554b0b51e",
                                               redirect_uri="http://127.0.0.1:9090",
                                               username=username,
                                               scope=scope))

# set the offset initially to zero
offset = 0

# set this to the number of songs 
max_songs = 372

# we need to keep calling get_song until we get all the songs in the user's library.
for song in range(offset, max_songs): 

	SpotifyClient.get_song(sp, offset)
	offset += 50



