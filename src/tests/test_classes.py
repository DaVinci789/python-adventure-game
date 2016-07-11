import unittest
from src import classes
from src import locations


class TestItem(classes.Item):

    def __init__(self):
        super().__init__("Itest", "a test", "moar test")


class CorrectArgsTest(unittest.TestCase):

    def test(self):
        test = locations.Location(
            "test", [], [], {}, "a test place", showNameWhenExit=True, dark=True)
        self.assertTrue(test)
