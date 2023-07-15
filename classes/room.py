from classes.song import Song
from classes.guest import Guest

class Room:
    def __init__(self,club,capacity):
        self.songs=[]
        self.club=club
        self.guests=[]
        self.capacity=capacity

    def check_out(self,guest):
        try:
            self.guests.remove(guest)
        except ValueError:
            pass

    def check_in(self,guest=str,wallet=0,fave_songs=[]):
        if len(self.guests)<self.capacity:
            if type(guest)==Guest:
                guest.add_fave_songs(fave_songs)
                [room.check_out(guest) for room in self.club.rooms]
                self.guests.append(guest)
            else:
                self.guests.append(Guest(guest,wallet,fave_songs))
                # Needs to pay club here but not sure how a room should refer to it's club
                # since the rooms exist in a list contained in club
                # & thats how they're connected so I don't wanna
                # pass the club into the check in method for rooms cause that feels messy.
                # I might have a fix later since I've been thinking of
                # getting rid of the rooms class & assimilating them into club.
        else:
            print("we're at capacity")
            return True

    def add_song(self,song=str):
        if song in self.songs or song in [room_song.name for room_song in self.songs]:
            return None
        if type(song)==list: # this should only ever happen when it's called by a guest adding their favourites
            self.songs+=song
        elif type(song)==str:
            self.songs.append(Song(song))