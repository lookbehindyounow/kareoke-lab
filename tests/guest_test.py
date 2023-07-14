import unittest
from classes.guest import Guest
from classes.room import Room
from classes.club import Club

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest=Guest("Kev",["Oasis","Happy Birthday"])
        self.club=Club("Great night kareoke")
        self.club.rooms=[Room(self.club) for i in range(10)]

    def test_has_attributes(self):
        self.assertEqual(self.guest.name,"Kev")
        self.assertEqual(self.guest.fave_songs,["Oasis","Happy Birthday"])

    def test_add_fave_songs(self):
        self.guest.add_fave_songs(["beetoven 14 sympony"])
        self.assertEqual(self.guest.fave_songs,["Oasis","Happy Birthday","beetoven 14 sympony"])

    def test_check_in(self):
        self.guest.check_in(self.club,0)
        self.assertEqual(self.club.rooms[0].guests,[self.guest])
        self.guest.check_in(self.club,1)
        self.assertEqual(self.club.rooms[1].guests,[self.guest])
        self.assertEqual(self.club.rooms[0].guests,[])

    def test_check_out(self):
        self.guest.check_in(self.club,0)
        self.assertEqual(self.club.rooms[0].guests,[self.guest])
        self.guest.check_out(self.club)
        self.assertEqual(self.club.rooms[0].guests,[])
