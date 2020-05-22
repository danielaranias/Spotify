

import sys,os
try:
    import spotipy
    import spotipy.util as util
except ImportError:
    raise ImportError('There is problem with importing Spotipy modules - use pip install spotipy')

# SPOTIPY_CLIENT_ID='B4f21284ad1d4859bdd778b67981f67b'
# SPOTIPY_CLIENT_SECRET='1155467e609e4d409adc03c14ba86742'
# SPOTIPY_REDIRECT_URI='https://osmooza.com/callback/'

class SpotifClient:
    """
    """
    def __init__(
        self,
        clientID,
        secretID,
        redirctURI,
        username
        ):
        """
        Taking the Cspotify client and secret IDs to connect Spotify
        clientID - your spotify client ID as you got it on regerstration
        secretID - clientID - your spotify secret ID as you got it on regerstration
        These are the token to use Spotify API
        """

        print('SpotifClient starts...')
        
        self.client_id = clientID
        self.secret_id = secretID
        self.redirect_uri = redirctURI
        self.username = username
        self._isConnected = False

        #self.Connect()
        
    def isConnected(self):
        return self._isConnected

    def Connect(self,scope):
        """
        Connecting to Spotify
        returing Spotify Client handle
        """

        """
        Calling util.prompt_for_user_token will open Spotify’s application authorization
        page in your browser (and require you to log in if you are not already logged in
        to spotify.com), unless a locally cached access token exist from a previous authorization/authentication.
        """
        try:
            token = util.prompt_for_user_token(
            self.username,
            scope,
            self.client_id,
            self.secret_id,
            self.redirect_uri)
        except ImportError:
            self._isConnected = False
            print(" onnecting to Spotify failed") 


        if token:
            sp = spotipy.Spotify(auth=token)
            self._isConnected = True
            return sp
        else:
            print("Can't get token for", self.username)
            self._isConnected = False 
        
        

