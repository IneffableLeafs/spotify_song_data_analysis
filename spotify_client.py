class SpotifyClient(object):

	# this function will return a list of the song ids of the user's spotify library
	def get_song_ids(client, offset, song_ids):

		# set our limit to 50 so each query gets 50 songs, the max for the spotipy function
		limit = 50
		results = client.current_user_saved_tracks(limit, offset)
		for idx, item in enumerate(results['items']):
			track = item['track']
			#print(idx + offset, track['artists'][0]['id'])
			song_ids.append(track['id'])

		return song_ids

	# this function will store nine audio features of all tracks in your library in separate lists
	def get_audio_features(client, song_id, danceability, energy, acousticness, valence, tempo):
		features = client.audio_features(song_id)

		# add each feature to its respective list
		danceability.append(features[0]['danceability'])
		energy.append(features[0]['energy'])
		acousticness.append(features[0]['acousticness'])
		valence.append(features[0]['valence'])
		tempo.append(features[0]['tempo'])