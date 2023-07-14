import unittest
from classes.guest import Guest
from classes.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest=Guest("Kev",["Oasis","Happy Birthday"])
        self.rooms=[Room() for i in range(10)]

    def test_has_attributes(self):
        self.assertEqual(self.guest.name,"Kev")
        self.assertEqual(self.guest.fave_songs,["Oasis","Happy Birthday"])

    def test_add_fave_songs(self):
        self.guest.add_fave_songs(["beetoven 14 sympony"])
        self.assertEqual(self.guest.fave_songs,["Oasis","Happy Birthday","beetoven 14 sympony"])

    def test_check_into_room(self):
        self.guest.check_into_room(self.rooms,0)
        self.assertEqual(self.rooms[0].guests,[self.guest])
        self.assertEqual(self.guest.room,0)
        self.guest.check_into_room(self.rooms,1)
        self.assertEqual(self.rooms[1].guests,[self.guest])
        self.assertEqual(self.rooms[0].guests,[])
        self.assertEqual(self.guest.room,1)