import unittest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room=Room(0) # thinking I'll have room numbers from 0 for easy indexing

    def test_has_attributes(self):
        self.assertEqual(self.room.number,0)
        self.assertEqual(self.room.songs,set())