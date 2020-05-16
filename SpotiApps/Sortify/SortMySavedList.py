
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
            self.show_tracks(results)
            while results['next']:
                results = self.sp_data.next(results)
                self.show_tracks(results)

            self.isSavedTracksAvailable =  True

        else:
            print('Failed to connect to Spotify')
            self.isSavedTracksAvailable =  False

    def show_tracks(self,results):
        for item in results['items']:
            track = item['track']
            print("%32.32s %s" % (track['artists'][0]['name'], track['name']))


