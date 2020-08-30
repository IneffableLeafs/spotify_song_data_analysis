class SpotifyClient(object):

	def get_song_ids(client, offset, song_ids):

		# set our limit to 50 so each query gets 50 songs, the max for the spotipy function
		limit = 50

		results = client.current_user_saved_tracks(limit, offset)
		for idx, item in enumerate(results['items']):
			track = item['track']
			#print(idx + offset, track['artists'][0]['id'])
			song_ids.append(track['artists'][0]['id'])

		return song_ids

	def audio_features():
		pass