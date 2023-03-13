# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class MusicTracks():
    # User-facing properties:
    #   name: string

    def __init__(self):
        
        # initialise an empty list
        pass # No code here yet

    def add_music_tracks(self, track):
        # Parameters:
        #   track: string representing a single music track
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the track to the self object
        pass # No code here yet

    def list_tracks(self):
        # Returns:
        #   A list of listened to music tracks
        # Side-effects:
        #   Passes a string advising of no tracks in list
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given no music tracks
We want to recieve a message stating no tracks in the list
"""
music_tracks = MusicTracks()
music_tracks.add_music_tracks()
music_tracks.list_tracks() # Return a message stating not tracks in list

"""
Given a number of music tracks, 
pass these to a list
return the list """

music_tracks = MusicTracks()
music_tracks.add_music_tracks("Thriller")
music_tracks.add_music_tracks("Bohemian rhapsody")
music_tracks.add_music_tracks("Take on me")
music_tracks.list_tracks() # Return a list with the three added music tracks

"""
Given an item that is not a string(music track)
I want to receive an Exception error
"""
music_tracks = MusicTracks()
music_tracks.add_music_tracks(123456) # Returns an Exception error

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


