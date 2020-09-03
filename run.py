import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from spotify_client import SpotifyClient
from data_analysis import DataAnalysis	
import pandas as pd
from matplotlib import pyplot as plt, dates
import seaborn as sns

scope = 'user-library-read user-read-recently-played playlist-modify-private playlist-read-private'

# authenticate and connect spotipy to spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="43dfe303cbce478e8c8952eed351e881",
                                               client_secret="3b8aa6ee50b64d9bb16ba09554b0b51e",
                                               redirect_uri="http://localhost:8888/callback",
                                               username="ineffableleaves",
                                               scope=scope))

# set the offset initially to zero
offset = 0

# 20 means the loop will cover 50x20 = 1000 songs:
max_songs = 20

# make lists for song ids, dates, recently played, whether the recent is in liked songs, and a list for new songs
song_ids = []
dates_added = []
song_ids, dates_added, recently_played_songs, in_liked_songs, new_songs = ([] for i in range(5))


# we need to keep calling get_song until we get all the songs in the user's library.
#for song in range(offset, max_songs): 
#	SpotifyClient.get_song_ids(sp, offset, song_ids, dates_added)
#	offset += 50

print(song_ids)
print(dates_added)


# now we need to loop through each track and get the audio features for each track, storing each feature in a separate list.
# we will consider the following features:
danceability, danceability_recent, energy, energy_recent, valence, valence_recent, tempo, tempo_recent = ([] for i in range(8))

# now, we want to hand the get_audio_features function a single track at once, then add its features to the respective list:
# also we want the dates that the track was added:
#for song_id in song_ids:
#	SpotifyClient.get_audio_features(sp, song_id, danceability, energy, valence, tempo)


# next, to do the data analysis with DataFrames, we need to convert our separate lists into a list of lists:
audio_features = []
audio_features.append(danceability)
audio_features.append(energy)
audio_features.append(valence)
audio_features.append(tempo)
audio_features.append(song_ids)
audio_features.append(dates_added)
#print(audio_features)

#df = DataAnalysis.dataframe_conversion(pd, audio_features)

# next, we need to look for new songs to add to my library.
# these songs must have my preferred features, or be in a reasonable boundary of these songs:
# we will need to use the current_user_saved_tracks_add(list of track ids) method.
# this means we need to first search spotify for tracks that match my taste, add them to a list of track ids,
# and then finally pass that list into the function.

SpotifyClient.recently_played(sp, song_ids, in_liked_songs, recently_played_songs)

# now lets get the audio features for our recently played songs:
#for recent_song in recently_played_songs:
#	SpotifyClient.get_audio_features(sp, recent_song, danceability_recent, energy_recent, valence_recent, tempo_recent)

# next, to do the data analysis with DataFrames, we need to convert our separate lists into a list of lists:
recent_audio_features = []
recent_audio_features.append(danceability_recent)
recent_audio_features.append(energy_recent)
recent_audio_features.append(valence_recent)
recent_audio_features.append(tempo_recent)
recent_audio_features.append(in_liked_songs)

#df_recents = DataAnalysis.recent_dataframe_conversion(pd, recent_audio_features)

# now we want to go through our dataframe of liked songs and get our "ideal songs":
# songs which fall into the bounds of the KDE plot highest density regions.
name = "audio_features.csv"
ideal_songs = DataAnalysis.ideal_song(pd, name)
# now, using this list of ideal songs, we need to get our list of recommendations:
# we will loop through so that we can get recommendations from all of our ideal songs:
SpotifyClient.recommended_songs(sp, ideal_songs, new_songs)

print(new_songs)
print(len(new_songs))

# create the playlist to put our recommended songs into
playlist = SpotifyClient.create_playlist(sp)

# add the recommended songs to our new playlist
SpotifyClient.add_songs(sp, playlist, new_songs)

