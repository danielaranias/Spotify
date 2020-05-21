
import os
import sys

secretID = os.environ['SPOTIPY_CLIENT_ID']
clientID = os.environ['SPOTIPY_CLIENT_SECRET']
redirectURI = os.environ['SPOTIPY_REDIRECT_URI']
username = os.environ['SPOTIPY_USERNAME']


sys.path.append('../')
from SpotiApps.SortifyApp.Sortify import Sortify

def test_read_saved_list():
    sp = Sortify(clientID, secretID, redirectURI, username)
    sp.readSavedTracks()
    assert sp.readSavedTracks != []