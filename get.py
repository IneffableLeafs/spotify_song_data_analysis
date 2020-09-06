from spotify_client import SpotifyClient
from data_analysis import DataAnalysis	
from spotipy_connection import sp
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# set the offset initially to zero
offset = 0

# 20 means the loop will cover 50x20 = 1000 songs:
max_songs = 20

# make lists for song ids, dates, recently played, whether the recent is in liked songs, and a list for new songs
song_ids = []
dates_added = []
song_ids, dates_added, recently_played_songs, in_liked_songs = ([] for i in range(4))


# we need to keep calling get_song until we get all the songs in the user's library.
for song in range(offset, max_songs): 
	SpotifyClient.get_song_ids(sp, offset, song_ids, dates_added)
	offset += 50

print("Obtained song IDS and dates successfully.")

# now we need to loop through each track and get the audio features for each track, storing each feature in a separate list.
# we will consider the following features:
danceability, danceability_recent, energy, energy_recent, valence, valence_recent, tempo, tempo_recent = ([] for i in range(8))

# now, we want to hand the get_audio_features function a single track at once, then add its features to the respective list:
for song_id in song_ids:
	SpotifyClient.get_audio_features(sp, song_id, danceability, energy, valence, tempo)
print("Obtained audio features of your songs successfully.")

# next, to do the data analysis with DataFrames, we need to convert our separate lists into a list of lists:
audio_features = []
audio_features.append(danceability)
audio_features.append(energy)
audio_features.append(valence)
audio_features.append(tempo)
audio_features.append(song_ids)
audio_features.append(dates_added)

# convert the audio_features list into a csv file
df = DataAnalysis.dataframe_conversion(pd, audio_features)
print("Created file 'audio_features.csv' successfully.")

# look at user's 50 most recently played songs
SpotifyClient.recently_played(sp, song_ids, in_liked_songs, recently_played_songs)
print("Obtained your 50 most recently played songs successfully.")


# now lets get the audio features for our recently played songs:
for recent_song in recently_played_songs:
	SpotifyClient.get_audio_features(sp, recent_song, danceability_recent, energy_recent, valence_recent, tempo_recent)
print("Obtained the audio features of your recently played songs successfully.")

# next, to do the data analysis with DataFrames, we need to convert our separate lists into a list of lists:
recent_audio_features = []
recent_audio_features.append(danceability_recent)
recent_audio_features.append(energy_recent)
recent_audio_features.append(valence_recent)
recent_audio_features.append(tempo_recent)
recent_audio_features.append(in_liked_songs)

df_recents = DataAnalysis.recent_dataframe_conversion(pd, recent_audio_features)
print("Created file 'recent_audio_features.csv' successfully.")

# you now need to analyze using plots.py to see your ideal_features manually,
# edit them in ideal_song() in data_analysis.py, and then run add.py.

