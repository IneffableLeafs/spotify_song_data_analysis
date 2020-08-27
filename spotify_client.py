import string
import requests

class SpotifyClient(object):
	def __init__(self, api_key):
		self.api_key = api_key

	def audio_features(self, id):
		url = "https://api.spotify.com/v1/audio-features/{id}"

		response = requests.get(
			url, 
			headers={
				"Content-Type": "application/json",
				"Authorization": f"Bearer {self.api_key}"
			}
		)
		
		response_json = response.json()

		tracks = [track for track in response_json['tracks']['items']]

		print(f'Found {len(tracks)} from spotify')

		return tracks