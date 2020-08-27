import string
import requests

class SpotifyClient(object):
	def __init__(self, BQDXQrUHOTDrG6rvF6xyZl8xhiSwXo33xV6t3uSEu1ixPh1daCGueZLAivAb2iY):
		self.api_key = api_key

	def audio_features(self, id):
		url = "https://api.spotify.com/v1/audio-features/{id}"

		# we need a way to get the id's of different songs,
		# most likely another function that returns a song id.
		# we then loop the audio_features function inside the get_song()
		


		response = requests.get(
			url, 
			headers={
				"Content-Type": "application/json",
				"Authorization": f"Bearer {self.api_key}"
			}
		)
		
		response_json = response.json()

		tracks = [track for track in response_json['tracks']['items']]

		print(f"Found {len(tracks)} from spotify")

		return tracks