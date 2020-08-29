import string
import requests

class SpotifyClient(object):
	def __init__(self, api_key):
		self.api_key = api_key


	def get_song(self):
		url = "https://api.spotify.com/v1/me/tracks"

		response = requests.get(
			url, 
			headers={
				"Accept": "application/json",
				"Content-Type": "application/json",
				#"Authorization": f"Bearer {self.api_key}"
				"Authorization": "Bearer BQC0kSUyR3-mcAGchwgO-Hdwkci2FEtM6v94bZldYg8EUqQGJFzQTBPHPr5-MiZerL7B5Arp_VccXtMCF9eVinoEU3bXVDfqUg36uCTaEiXH9OwtzdNdPIbGC9TZCZbyiJNzFp6K9-1dzLLzL-ZKResR86zD3ZGj"
			}
		)

		response_json = response.json()
		tracks = [track for track in response_json['items']['id']]
		print(f"Found {len(tracks)} from your spotify")

		return tracks



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