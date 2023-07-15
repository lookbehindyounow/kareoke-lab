import unittest
from classes.guest import Guest
from classes.room import Room
from classes.club import Club
from classes.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.test_songs=[Song("Oasis"),Song("Happy Birthday")]
        self.guest=Guest("Kev",self.test_songs)
        self.club=Club("Great night kareoke")
        self.club.rooms=[Room(self.club,10) for i in range(10)]

    def test_has_attributes(self):
        self.assertEqual(self.guest.name,"Kev")
        self.assertEqual(self.guest.fave_songs,self.test_songs)

    def test_add_fave_songs(self):
        local_test_song=Song("beetoven 14 sympony")
        self.guest.add_fave_songs([local_test_song])
        self.assertEqual(self.guest.fave_songs[2].name,"beetoven 14 sympony")

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

    def test_add_songs_to_room(self):
        self.guest.check_in(self.club,0)
        self.assertEqual(self.club.rooms[0].guests,[self.guest])
        self.guest.add_songs_to_room(self.club)
        self.assertEqual(self.guest.fave_songs,self.club.rooms[0].songs)
        self.guest.add_songs_to_room(self.club,"beetoven 14 sympony")
        self.assertEqual(self.club.rooms[0].songs[2].name,"beetoven 14 sympony")

    def test_capacity_check(self):
        self.guest2=Guest("Dan")
        temp_guests=[Guest(str(i),[]) for i in range(10)]
        [guest.check_in(self.club,0) for guest in temp_guests]
        self.assertEqual(len(self.club.rooms[0].guests),10)
        self.guest2.check_in(self.club,0) # 11th guest
        self.assertEqual(len(self.club.rooms[0].guests),10)