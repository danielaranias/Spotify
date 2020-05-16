
import os
import sys

sys.path.append('../')
from SpotiApps.Sortify.SortMySavedList import SortMySavedList

def test_read_saved_list():
    sp = SortMySavedList()
    sp.readSavedTracks()
    assert sp.readSavedTracks != []