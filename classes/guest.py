class Guest:
    def __init__(self,name=str,fave_songs=list):
        self.name=name
        self.fave_songs=fave_songs

    def add_fave_songs(self,songs=list):
        self.fave_songs+=songs

    def check_into_room(self,rooms=list,number=int):
        self.room=number
        rooms[number].check_in_guest(self)