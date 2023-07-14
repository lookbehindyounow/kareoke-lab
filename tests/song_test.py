import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song=Song("Oasis")

    def test_has_attributes(self):
        self.assertEqual(self.song.name,"Oasis")