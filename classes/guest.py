class Guest:
    def __init__(self,name=str,fave_songs=list):
        self.name=name
        self.fave_songs=fave_songs

    def add_fave_songs(self,songs=list):
        self.fave_songs+=songs

    def check_in(self,club,number=int):
        club.rooms[number].check_in(self)

    def check_out(self,club):
        club.check_out(self)

    def add_songs_to_room(self,club,song=""):
        room=[i for i in range(len(club.rooms)) if self in club.rooms[i].guests][0]
        if song=="": # if called without passing an argument for songs,
            club.rooms[room].add_song(self.fave_songs) # it adds the guests favourites
        else:
            club.rooms[room].add_song(song)