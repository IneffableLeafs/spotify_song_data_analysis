import os
from spotify_client import SpotifyClient


def run():
	# Search the user's Spotify for liked songs
	spotify_client = SpotifyClient(os.getenv("SPOTIFY_AUTH_TOKEN"))
	track_info = spotify_client.audio_features()
