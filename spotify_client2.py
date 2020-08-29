import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SpotifyClient(object):

	def get_song(self):
		scope = "user-library-read"
		sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

		results = sp.current_user_saved_tracks()
		for idx, item in enumerate(results['items']):
		    track = item['track']
		    print(idx, track['artists'][0]['name'], " – ", track['name'])


	def audio_features(self):
		pass
