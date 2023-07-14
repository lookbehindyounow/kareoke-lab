import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

# Thinking I'll have room numbers be represented by the index of
# a list of rooms, could maybe be a tuple? would have to experiment
class TestRoom(unittest.TestCase):
    def setUp(self):
        self.rooms=[Room() for i in range(10)]
        # tried [Room()]*10 but it just filled every index
        # with the same instance of Room

    def test_has_attributes(self):
        self.assertEqual(self.rooms[0].songs,set())
        self.assertEqual(self.rooms[0].guests,[])

    def test_check_in_guest(self):
        self.rooms[0].check_in_guest("Kev",["Oasis","Happy Birthday"])
        self.rooms[0].check_in_guest("Kev who forgot what music he likes")
        self.rooms[1].check_in_guest("Kev who hates music",[])
        self.assertEqual(self.rooms[0].guests[0].name,"Kev")
        self.assertEqual(self.rooms[0].guests[0].fave_songs,["Oasis","Happy Birthday"])
        self.assertEqual(self.rooms[0].guests[1].name,"Kev who forgot what music he likes")
        self.assertEqual(self.rooms[0].guests[1].fave_songs,[])
        self.assertEqual(self.rooms[1].guests[0].name,"Kev who hates music")
        self.assertEqual(self.rooms[1].guests[0].fave_songs,[])