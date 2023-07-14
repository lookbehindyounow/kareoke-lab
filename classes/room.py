from classes.song import Song

class Room:
    def __init__(self,number=int):
        self.number=number
        self.songs=set()

    # I want this method to be able to create a guest
    # but I also want a guest to be able to call it &
    # check in themselves.
    def check_in_guest(guest,fave_songs=[]):
        pass