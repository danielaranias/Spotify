import sys,os
from SortifyApp.Sortify import Sortify


SPOTIPY_CLIENT_ID = 'B4f21284ad1d4859bdd778b67981f67b'
SPOTIPY_CLIENT_SECRET ='1155467e609e4d409adc03c14ba86742'
SPOTIPY_REDIRECT_URI ='https://osmooza.com/callback/'
SPOTIPY_USERNAME ='d2k6pyuiogq6ph8ap0gg596ub'


sort = Sortify(SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI,SPOTIPY_USERNAME)
saved_list = sort.readSavedTracks()
sort.showTracks(saved_list)

