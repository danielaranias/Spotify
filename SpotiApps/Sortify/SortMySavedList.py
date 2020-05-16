
import os
import sys

sys.path.append('../')

from SpotiApps.SpotifyAPI import SpotifyClient


class SortMySavedList():
    """
    This class connects to Spotify user account and sort the Saved/Liked tracks list
    """

    def __init__(self):
        self.sp_client = SpotifyClient.SpotifClient()
        self.isSavedTracksAvailable = False
        

    def readSavedTracks(self):
        """
        """
        username = 'd2k6pyuiogq6ph8ap0gg596ub'
        scope = 'user-library-read'
        self.sp_data = self.sp_client.Connect(username,scope)
        if self.sp_client.isConnected() == True:
            print('We are connected to Spotify!!!!')
            
            results = self.sp_data.current_user_saved_tracks()
            for item in results['items']:
                track = item['track']
                print(track['name'] + ' - ' + track['artists'][0]['name'])

            self.isSavedTracksAvailable =  True

        else:
            print('Failed to connect to Spotify')
            self.isSavedTracksAvailable =  False


