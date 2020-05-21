
import os
import sys

sys.path.append('../')
from SpotiApps.SpotifyAPI import SpotifyClient

secretID = os.environ['SPOTIPY_CLIENT_ID']
clientID = os.environ['SPOTIPY_CLIENT_SECRET']
redireXctURI = os.environ['SPOTIPY_REDIRECT_URI']
username = os.environ['SPOTIPY_USERNAME']

def test_connecting_to_spotify_API_with_wrong_token():
    ClientID = '###'
    SecretID = '@@@'
    sp = SpotifyClient.SpotifClient(clientID,secretID,redirctURI,username)
    assert sp.isConnected() == False


def test_connecting_to_spotify_API_with_correct_token():

    
    scope = 'user-library-read'

    sp = SpotifyClient.SpotifClient(clientID,secretID)
    sp.Connect(username,scope)
    assert sp.isConnected() == True

