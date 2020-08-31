import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from spotify_client import SpotifyClient
from data_analysis import DataAnalysis	
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# make a list to put our song ids into
song_ids = []

print("Depending on the size of library, this may take a few minutes.")
# we need to keep calling get_song until we get all the songs in the user's library.
#for song in range(offset, max_songs): 

SpotifyClient.get_song_ids(sp, offset, song_ids)
	#offset += 50

print(song_ids)
# now we need to loop through each track and get the audio features for each track, storing each feature in a separate list.
# we will consider the following features:
danceability, energy, acousticness, valence, tempo = ([] for i in range(9))

# now, we want to hand the get_audio_features function a single track at once, then add its features to the respective list:
for song_id in song_ids:
	SpotifyClient.get_audio_features(sp, song_id, danceability, energy, acousticness, valence, tempo)

# next, to do the data analysis with DataFrames, we need to convert our separate lists into a list of lists:
audio_features = []
audio_features.append(danceability)
audio_features.append(energy)
audio_features.append(acousticness)
audio_features.append(valence)
audio_features.append(tempo)

df = DataAnalysis.dataframe_conversion(pd, audio_features)





