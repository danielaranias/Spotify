
import os
import sys

sys.path.append('../')
from SpotiApps.SpotifyAPI import SpotifyClient



def test_connecting_to_spotify_API_with_wrong_token():
    ClientID = '###'
    SecretID = '@@@'
    sp = SpotifyClient.SpotifClient(ClientID,SecretID)
    assert sp.isConnected() == False


def test_connecting_to_spotify_API_with_correct_token():

    username = os.environ['SPOTIPY_USERNAME']
    clientID= os.environ['SPOTIPY_CLIENT_ID']
    secretID= os.environ['SPOTIPY_CLIENT_SECRET']
    scope = 'user-library-read'

    sp = SpotifyClient.SpotifClient(clientID,secretID)
    sp.Connect(username,scope)
    assert sp.isConnected() == True

