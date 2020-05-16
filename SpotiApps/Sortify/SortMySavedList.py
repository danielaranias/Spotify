
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
        
    def printSavedTracked(self):
        self.show_tracks(self.saved_tracks_list)

        #showing also after the limit (20)
        # while self.saved_tracks['next']:
        #     results = self.sp_data.next(self.saved_tracks)
        #     self.show_tracks(results)

    def readSavedTracks(self)->'list':
        """
        returns list of all tracks (need also to read the 'next' for getting ALL tracks) 
        """
        username = 'd2k6pyuiogq6ph8ap0gg596ub'
        scope = 'user-library-read'
        self.saved_tracks_list = []
        self.sp_data = self.sp_client.Connect(username,scope)
    
        if self.sp_client.isConnected() == True:
            print('We are connected to Spotify!!!!')
            
            tracks = self.sp_data.current_user_saved_tracks()
            self.saved_tracks_list = tracks['items']
            while tracks['next']:
                self.saved_tracks_list += self.sp_data.next(tracks)['items']
            
            self.isSavedTracksAvailable =  True
            

        else:
            print('Failed to connect to Spotify')
            self.isSavedTracksAvailable =  False

        return self.saved_tracks_list

    def showTracks(self,results):
        for item in results:
            track = item['track']
            print("%32.32s %s" % (track['artists'][0]['name'], track['name']))


