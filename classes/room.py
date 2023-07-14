from classes.song import Song
from classes.guest import Guest

class Room:
    def __init__(self):
        self.songs=set()
        self.guests=[]

    def check_in_guest(self,guest,fave_songs=[]):
        if type(guest)==Guest:
            guest.add_fave_songs(fave_songs)
            self.guests.append(guest)
        else:
            self.guests.append(Guest(guest,fave_songs))