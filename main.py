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
    lo_lat : float
    hi_lat : float
    west_long : float
    east_long : float

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
    ghg_rate : float #in million metric tons of C02 equivalent per year

region1 : RegionCondition = RegionCondition(Region(GlobeRect(47.49616, 47.73464, -122.43689, -122.23591), "Seattle", "Port City"), 2022, 751454, 2.98)
region2 : RegionCondition = RegionCondition(Region(GlobeRect(44.47121, 44.57550, -88.14111, -87.84214), "Green Bay", "Port City"), 2018, 104756, 2.78)
region3 : RegionCondition = RegionCondition(Region(GlobeRect(34.62524, 52.01460, -155.43856, -132.83251), "North Pacific", "Ocean"), 2020, 0, 0.0)
region4 : RegionCondition = RegionCondition(Region(GlobeRect(35.23421, 35.31154, -120.72305, -120.61785), "SLO", "Agriculture City"), 2021, 47545, 0.151)

example_region_conditions : List[RegionCondition] = [region1, region2, region3, region4]

# put all test cases in the "Tests" class.
class Tests(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(14,14)


if (__name__ == '__main__'):
    unittest.main()
