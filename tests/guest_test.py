import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest=Guest("Kev")

    def test_has_attributes(self):
        self.assertEqual(self.guest.name,"Kev")