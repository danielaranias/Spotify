
import os
import sys
import pandas as pd

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
        self.sp_data = self.sp_client.Connect(scope)
    
        
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
    def tracksToDataFrame(self,tracksList)->"dataframe":
        """
            "duration_ms" : 255349,
            "key" : 5,
            "mode" : 0,
            "time_signature" : 4,
            "acousticness" : 0.514,
            "danceability" : 0.735,
            "energy" : 0.578,
            "instrumentalness" : 0.0902,
            "liveness" : 0.159,
            "loudness" : -11.840,
            "speechiness" : 0.0461,
            "valence" : 0.624,
            "tempo" : 98.002,
            "id" : "06AKEBrKUckW0KREUWRnvT",
            "uri" : "spotify:track:06AKEBrKUckW0KREUWRnvT",
            "track_href" : 
        """
        
        track_features_list = []
        tracks_ids = []
        tracks_names = []
        
        
        #collecting all IDs for getting later the features
        for item in tracksList:
            tracks_ids.append(item['track']['id'])
            tracks_names.append(item['track']['name'])
        

        #calling to spotify API to get tracks features (MAX 100) - much faster than one by one
        track_index = 0
        tracks_len = len(tracks_ids)
    
        for track_index in range(0, tracks_len, 100):
            track_features_list += self.sp_data.audio_features(tracks_ids[track_index:(track_index+100)])
            

        df = pd.DataFrame(track_features_list)
        df['track name'] = tracks_names
        

        return df

        

    def showTracks(self,results):
        for item in results:
            track = item['track']
            print("%32.32s %s" % (track['artists'][0]['name'], track['name']))


