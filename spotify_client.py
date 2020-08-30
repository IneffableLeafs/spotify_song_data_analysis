class SpotifyClient(object):

	def get_song(client):

		results = client.current_user_saved_tracks()
		print(results)
		for idx, item in enumerate(results['items']):
			track = item['track']
			print(idx, track['artists'][0]['name'], " – ", track['name'])
