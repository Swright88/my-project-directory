from lib.music_tracks import *
import pytest

def test_no_tracks_added():
    music_track = MusicTracks()
    assert  music_track.list_tracks() == "No tracks added to list"
    
def test_list_tracks():
    music_track = MusicTracks()
    music_track.add_music_tracks("Thriller")
    music_track.add_music_tracks("Bohemian rhapsody")
    music_track.add_music_tracks("Take on me")
    assert  music_track.list_tracks() == ["Thriller", "Bohemian rhapsody", "Take on me"]
    
    
def test_wrong_type_entered():
    music_track = MusicTracks()
    with pytest.raises(Exception) as e:
        music_track.add_music_tracks(123456)
    error_message = str(e.value)
    assert error_message == "This is not a string type"