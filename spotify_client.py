class SpotifyClient(object):

	def get_song(client, offset):

		limit = 50
		results = client.current_user_saved_tracks(limit, offset)
		#library = results["total"]
		for idx, item in enumerate(results['items']):
			track = item['track']
			print(idx + offset, track['artists'][0]['name'], " – ", track['name'])