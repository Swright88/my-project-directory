class MusicTracks():
    def __init__(self):
        self.music_list = []
        pass
    
    def add_music_tracks(self, track):
        self.track = track
        if type(track) is not str:
            raise Exception("This is not a string type")
        else:
            self.music_list.append(self.track)
        
    def list_tracks(self):
        if len(self.music_list) == 0:
            return("No tracks added to list")
        else:
            return(self.music_list)