from classes.club import Club

class Guest:
    def __init__(self,name=str,fave_songs=list):
        self.name=name
        self.fave_songs=fave_songs

    def add_fave_songs(self,songs=list):
        self.fave_songs+=songs

    def check_in(self,club=Club,number=int):
        club.rooms[number].check_in(self)

    def check_out(self,club=Club):
        club.check_out(self)