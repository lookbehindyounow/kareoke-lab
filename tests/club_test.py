import unittest
from classes.club import Club
from classes.room import Room

class TestClub(unittest.TestCase):
    def setUp(self):
        self.club=Club("Great night kareoke")
        self.club.rooms=[Room(self.club) for i in range(10)]

    def test_check_out(self):
        self.club.rooms[0].check_in("Kev",["Oasis","Happy Birthday"])
        self.club.check_out(self.club.rooms[0].guests[0])
        self.assertEqual(self.club.rooms[0].guests,[])