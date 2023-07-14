import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room=Room(0) # thinking I'll have room numbers from 0 for easy indexing

    def test_has_attributes(self):
        self.assertEqual(self.room.number,0)
        self.assertEqual(self.room.songs,set())

    def test_check_in_guest(self):
        self.room.check_in_guest("Kev",["Oasis"])
        self.room.check_in_guest("Imaginary Kev")
        self.room.check_in_guest("Imaginary Kev",[])
        self.room.check_in_guest("Kev who hates music",["None"])