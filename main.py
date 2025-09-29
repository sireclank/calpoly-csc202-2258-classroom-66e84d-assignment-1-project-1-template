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
    #latitudes must be from -90.0 to 90.0
    lo_lat = float #must be lower than hi_lat
    hi_lat = float
    
    #longitudes must be from -180.0 to 180.0
    #if west_long == east_long, then width = 0
    west_long = float
    east_long = float

#Creates a class that takes a rectangle from GlobeRect and describes it
@dataclass(frozen=True)
class Region:
    rect : GlobeRect #the area of the specific GlobeRect
    name : str #The name of the region
    terrain : str #being the type of terrain/biome (ie forest, mountain, etc)

#Creates a class that holds the details of a specific region
@dataclass(frozen=True)
class RegionCondition:
    region : Region
    year : int #The year of the region
    pop : int #The population of people in the region
    ghg_rate : float #in tons of C02 equivalent per year

#This function describes the region condition of Seattle, WA
def Seattle(reg:RegionCondition):


# put all test cases in the "Tests" class.
class Tests(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(14,14)


if (__name__ == '__main__'):
    unittest.main()
