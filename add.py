from run import pd, sp, ideal_songs, new_songs

# from looking at the KDE plots in plots.py, the darkest regions were in what bounds?
max_energy = 0.8
min_energy = 0.6
max_valence = 0.63
min_valence = 0.47
max_tempo = 133
min_tempo = 77


# now we want to go through our dataframe of liked songs and get our "ideal songs":
# songs which fall into the bounds of the KDE plot highest density regions.
name = "audio_features.csv"
ideal_songs = DataAnalysis.ideal_song(pd, name, max_energy, max_valence, max_tempo, min_energy, min_valence, min_tempo)
# now, using this list of ideal songs, we need to get our list of recommendations:
# we will loop through so that we can get recommendations from all of our ideal songs:
SpotifyClient.recommended_songs(sp, ideal_songs, new_songs)

print(new_songs)
print(len(new_songs))

# create the playlist to put our recommended songs into
playlist = SpotifyClient.create_playlist(sp)

# add the recommended songs to our new playlist
SpotifyClient.add_songs(sp, playlist, new_songs)