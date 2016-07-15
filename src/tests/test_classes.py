import unittest
from src import classes
from src import locations


class TestItem(classes.Item):

    def __init__(self):
        super().__init__("Itest", "a test", "moar test")


class CorrectArgsTest(unittest.TestCase):

    def test(self):
        test_location = locations.Location(
            "test_location", [], [], {}, "a test_location place", showNameWhenExit=True, dark=True)
        test_player = classes.Player(
            locations.Location_Storage, locations.start)
        self.assertTrue(test_location)
        self.assertTrue(TestItem())
        self.assertTrue(test_player)
