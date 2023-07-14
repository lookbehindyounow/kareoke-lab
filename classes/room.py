from classes.song import Song
from classes.guest import Guest

class Room:
    def __init__(self,club):
        self.songs=[]
        self.club=club
        self.guests=[]

    def check_out(self,guest):
        try:
            self.guests.remove(guest)
        except ValueError:
            pass

    def check_in(self,guest=str,fave_songs=[]):
        if type(guest)==Guest:
            guest.add_fave_songs(fave_songs)
            [room.check_out(guest) for room in self.club.rooms]
            self.guests.append(guest)
        else:
            self.guests.append(Guest(guest,fave_songs))

    def add_song(self,song=str):
        if song in self.songs or song in [room_song.name for room_song in self.songs]:
            return None
        if type(song)==list: # this should only ever happen when it's called by a guest adding their favourites
            self.songs+=song
        elif type(song)==str:
            self.songs.append(Song(song))