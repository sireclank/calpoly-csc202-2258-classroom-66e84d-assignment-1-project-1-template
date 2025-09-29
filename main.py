from typing import *
from dataclasses import dataclass
import unittest
import math
import sys
sys.setrecursionlimit(10**6)

calpoly_email_addresses = ["jjmazza@calpoly.edu"]

#Creates a class for rectangles on a globe
@dataclass(frozen=True)
class GlobeRect:
    #latitudes must be from -90 to 90
    lo_lat = int #must be lower than hi_lat
    hi_lat = int
    #longitudes must be from -180 to 180
    #if west_long == east_long, then width = 0
    west_long = int
    east_long = int

#Creates a class that takes a rectangle from GlobeRect and describes it
@dataclass(frozen=True)
class Region:
    area : GlobeRect
    name : str
    terrain : str

# put all test cases in the "Tests" class.
class Tests(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(14,14)


if (__name__ == '__main__'):
    unittest.main()
