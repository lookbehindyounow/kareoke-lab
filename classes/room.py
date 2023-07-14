from classes.song import Song
from classes.guest import Guest

class Room:
    def __init__(self,club):
        self.songs=set()
        self.club=club
        self.guests=[]

    def check_out(self,guest):
        try:
            self.guests.remove(guest)
        except ValueError:
            pass

    def check_in(self,guest,fave_songs=[]):
        if type(guest)==Guest:
            guest.add_fave_songs(fave_songs)
            [room.check_out(guest) for room in self.club.rooms]
            self.guests.append(guest)
        else:
            self.guests.append(Guest(guest,fave_songs))