import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from spotify_client import SpotifyClient
from data_analysis import DataAnalysis	
import pandas as pd
from matplotlib import pyplot as plt, dates
import seaborn as sns

scope = 'user-library-read'

# authenticate and connect spotipy to spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="43dfe303cbce478e8c8952eed351e881",
                                               client_secret="3b8aa6ee50b64d9bb16ba09554b0b51e",
                                               redirect_uri="http://localhost:8888/callback",
                                               username="ineffableleaves",
                                               scope=scope))

# set the offset initially to zero
offset = 0

# set this to the number of songs 
max_songs = 372

# make a list to put our song ids into and dates
song_ids = []
dates_added = []

# we need to keep calling get_song until we get all the songs in the user's library.
for song in range(offset, max_songs): 
	SpotifyClient.get_song_ids(sp, offset, song_ids, dates_added)
	offset += 50

print(song_ids)
print(dates_added)


# now we need to loop through each track and get the audio features for each track, storing each feature in a separate list.
# we will consider the following features:
danceability, energy, valence, tempo = ([] for i in range(4))

# now, we want to hand the get_audio_features function a single track at once, then add its features to the respective list:
# also we want the dates that the track was added:
for song_id in song_ids:
	SpotifyClient.get_audio_features(sp, song_id, danceability, energy, valence, tempo)


# next, to do the data analysis with DataFrames, we need to convert our separate lists into a list of lists:
audio_features = []
audio_features.append(danceability)
audio_features.append(energy)
audio_features.append(valence)
audio_features.append(tempo)
audio_features.append(dates_added)

df = DataAnalysis.dataframe_conversion(pd, audio_features)





