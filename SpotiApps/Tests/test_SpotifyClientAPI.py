
import os
import sys

sys.path.append('../')
from SpotiApps.SpotifyAPI import SpotifyClient

SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
SPOTIPY_REDIRECT_URI = os.environ['SPOTIPY_REDIRECT_URI']
SPOTIPY_USERNAME = os.environ['SPOTIPY_USERNAME']


def test_connecting_to_spotify_API_with_correct_token():

    scope = 'user-library-read'

    sp = SpotifyClient.SpotifClient(
        SPOTIPY_CLIENT_ID,
        SPOTIPY_CLIENT_SECRET,
        SPOTIPY_REDIRECT_URI,
        SPOTIPY_USERNAME)

    sp.Connect(scope)
    assert sp.isConnected() == True

