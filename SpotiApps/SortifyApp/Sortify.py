
import os
import sys

sys.path.append('../')

from SpotiApps.SpotifyAPI import SpotifyClient


class Sortify():
    """
    This class connects to Spotify user account and sort the Saved/Liked tracks list
    """

    def __init__(
        self,
        clientID,
        secretID,
        redirctURI,
        username
        ):
        self.sp_client = SpotifyClient.SpotifClient(clientID,secretID,redirctURI,username)
        self.username = username
        self.isSavedTracksAvailable = False
        
    def printSavedTracked(self):
        self.showTracks(self.saved_tracks_list)

        

    def readSavedTracks(self)->'list':
        """
        returns list of all tracks (need also to read the 'next' for getting ALL tracks) 
        """
        scope = 'user-library-read'
        self.saved_tracks_list = []
        self.sp_data = self.sp_client.Connect(self.username,scope)
    
        
        if self.sp_client.isConnected() == True:
            print('We are connected to Spotify!!!!')

            try:

                tracks_index = self.sp_data.current_user_saved_tracks()
                #adding tracks to the list
                self.saved_tracks_list = tracks_index['items']
                while tracks_index['next']:
                    #reading and adding the Next tracks into the tracks list 
                    self.saved_tracks_list += self.sp_data.next(tracks_index)['items']
                    # increasing the index to the correct placxe
                    tracks_index = self.sp_data.next(tracks_index)
                
                self.isSavedTracksAvailable =  True

            except ImportError:
                raise ImportError('There was a problem reading all the track list!!')
            
        else:
            print('Failed to connect to Spotify')
            self.isSavedTracksAvailable =  False

        return self.saved_tracks_list

    def showTracks(self,results):
        for item in results:
            track = item['track']
            print("%32.32s %s" % (track['artists'][0]['name'], track['name']))


