import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
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

# authenticate for audio features
client_credentials_manager = SpotifyClientCredentials()
sp2 = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# set the offset initially to zero
offset = 0

# set this to the number of songs 
max_songs = 372

# make a list to put our song ids into
song_ids = []

print("Depending on the size of library, this may take a few minutes.")
# we need to keep calling get_song until we get all the songs in the user's library.
for song in range(offset, max_songs): 

	SpotifyClient.get_song_ids(sp, offset, song_ids)
	offset += 50

# now we need to loop through each track and get the audio features for each track, storing each feature in a separate list.
# we will consider the following features:
danceability, energy, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo = ([] for i in range(9))

# now, we want to hand the get_audio_features function a single track at once, then add its features to the respective list:
#for song_id in song_ids:

for song_id in song_ids:
	SpotifyClient.get_audio_features(sp2, song_id, danceability, energy, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo)



