class SpotifyClient(object):

	# this function will return a list of the song ids of the user's spotify library and the dates added
	def get_song_ids(client, offset, song_ids, dates_added):

		# set our limit to 50 so each query gets 50 songs, the max for the spotipy function
		limit = 50
		results = client.current_user_saved_tracks(limit, offset)
		for idx, item in enumerate(results['items']):
			track = item['track']
			added_at = item['added_at']
			added_at = added_at[0:10]

			print(idx + offset, track['id'] + " - " + track['name'])
			song_ids.append(track['id'])
			dates_added.append(added_at)


	# this function will store four audio features of a track in your library in separate lists
	def get_audio_features(client, song_id, danceability, energy, valence, tempo):
		features = client.audio_features(song_id)

		# add each feature to its respective list
		danceability.append(features[0]['danceability'])
		energy.append(features[0]['energy'])
		valence.append(features[0]['valence'])
		tempo.append(features[0]['tempo'])

	# this function will look at recently played songs and determine if it is in our liked songs
	def recently_played(client, song_ids, in_liked_songs, recently_played_songs):

		# set our limit to 50 so each query gets 50 songs, the max for the spotipy function
		limit = 50
		results = client.current_user_recently_played(limit)
		for idx, item in enumerate(results['items']):
			track = item['track']
			print(idx, track['id'] + " - " + track['name'])
			recently_played_songs.append(track['id'])

			# if our track is found in our liked songs:
			if song_ids.count(track['id']) == 1:
				in_liked_songs.append(1) # 1 if song is liked
			else:
				in_liked_songs.append(0) # 0 if song is not liked

	# this function will get recommendations from spotify that match my feature criteria: 				
	def recommended_songs(client, ideal_songs, new_songs):
		# get the 3 most recently added songs for the seed
		for song in ideal_songs:
		#ideal_songs = ideal_songs[:3]
			print(song)
			song = [song]
			print(song)
			recom_songs = client.recommendations(limit=100, seed_tracks=song)
			print(recom_songs)
			for idx, track in enumerate(recom_songs['tracks']):
				new_track = track['id']
				print(idx, track['id'] + " - " + track['name'])
				new_songs.append(track['id'])

	# create a playlist to put our recommended songs into, get the playlist id:
	def create_playlist(client):
		# first, lets create the playlist:
		user_id = "ineffableleaves"
		playlist_name = "DataPlaylist"
		client.user_playlist_create(user_id, playlist_name, public=False, collaborative=False, description="This playlist was created with Python.")
		playlists = client.user_playlists(user_id, limit=50, offset=0)
		# now, let's get the ID of that playlist:
		for playlist in enumerate(playlists['items']):
			name = playlist['name']
			if name == playlist_name:
				playlist_id = playlist['id']
				break
			else: 
				continue
				
		return playlist_id


	# this function will add our recommended songs to our spotify library:
	def add_songs(client, new_songs):
		playlist_add_items(playlist_id, items, position=None)


