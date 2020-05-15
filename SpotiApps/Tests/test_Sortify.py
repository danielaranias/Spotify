
import os
import sys

sys.path.append('../')
from SpotiApps.Sortify.SpotifyAPI import SortSongs as SS


def test_A():
    b = SS()
    assert b.isPlaylistSorted() == True