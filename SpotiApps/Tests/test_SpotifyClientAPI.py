
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
    ClientID = 'B4f21284ad1d4859bdd778b67981f67b'
    SecretID = '1155467e609e4d409adc03c14ba86742'
    username = 'd2k6pyuiogq6ph8ap0gg596ub'
    scope = 'user-library-read'

    sp = SpotifyClient.SpotifClient(ClientID,SecretID)
    sp.Connect(username,scope)

    assert sp.isConnected() == True

