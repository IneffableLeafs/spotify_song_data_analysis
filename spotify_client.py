import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SpotifyClient(object):

	def get_song(self, client):

	results = sp.current_user_saved_tracks()
	print(results)
	for idx, item in enumerate(results['items']):
    	track = item['track']
    	print(idx, track['artists'][0]['name'], " – ", track['name'])


	def audio_features(self, song):
		pass
