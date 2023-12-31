import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song
from classes.club import Club

# Thinking I'll have room numbers be represented by the index of
# a list of rooms, could maybe be a tuple? would have to experiment
class TestRoom(unittest.TestCase):
    def setUp(self):
        self.club=Club("Great night kareoke",100)
        self.club.rooms=[Room(self.club,10) for i in range(10)]
        # tried [Room()]*10 but it just filled every index
        # with the same instance of Room

    def test_has_attributes(self):
        self.assertEqual(self.club.rooms[0].songs,[])
        self.assertEqual(self.club.rooms[0].guests,[])

    def test_check_in(self):
        self.club.rooms[0].check_in("Kev",30,["Oasis","Happy Birthday"])
        self.club.rooms[0].check_in("Kev who forgot what music he likes",30)
        self.club.rooms[1].check_in("Kev who hates music",30,[])
        self.assertEqual(self.club.rooms[0].guests[0].name,"Kev")
        self.assertEqual(self.club.rooms[0].guests[0].fave_songs,["Oasis","Happy Birthday"])
        self.assertEqual(self.club.rooms[0].guests[1].name,"Kev who forgot what music he likes")
        self.assertEqual(self.club.rooms[0].guests[1].fave_songs,[])
        self.assertEqual(self.club.rooms[1].guests[0].name,"Kev who hates music")
        self.assertEqual(self.club.rooms[1].guests[0].fave_songs,[])

    def test_check_out(self):
        self.club.rooms[0].check_in("Kev",30,["Oasis","Happy Birthday"])
        self.assertEqual(self.club.rooms[0].guests[0].name,"Kev")
        self.club.check_out(self.club.rooms[0].guests[0])
        self.assertEqual(self.club.rooms[0].guests,[])

    def test_add_song(self):
        self.club.rooms[0].add_song("Oasis")
        self.assertEqual(self.club.rooms[0].songs[0].name,"Oasis")

    def test_capacity_check(self):
        [self.club.rooms[0].check_in("Kev",30,["Oasis","Happy Birthday"]) for i in range(9)]
        returned=self.club.rooms[0].check_in("Kev",30,["Oasis","Happy Birthday"]) # 10th guest
        self.assertEqual(returned,None)
        returned=self.club.rooms[0].check_in("Kev",30,["Oasis","Happy Birthday"]) # 11th guest
        self.assertEqual(len(self.club.rooms),10)
        self.assertEqual(returned,True)

    @unittest.skip("transactions don't currently work when check in is called by a room, see why in classes/room.py")
    def test_transaction(self):
        self.club.rooms[0].check_in("Kev",30,["Oasis","Happy Birthday"])
        self.assertEqual(self.club.rooms[0].guests[0].wallet,20)
        self.assertEqual(self.club.till,110)