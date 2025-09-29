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
    ghg_rate : float 

region1 : RegionCondition = RegionCondition(Region(GlobeRect(47.49616, 47.73464, -122.43689, -122.23591), "Seattle", "Port City"), 2022, 751454, 2980000.0)
region2 : RegionCondition = RegionCondition(Region(GlobeRect(44.47121, 44.57550, -88.14111, -87.84214), "Green Bay", "Port City"), 2018, 104756, 2780000.0)
region3 : RegionCondition = RegionCondition(Region(GlobeRect(34.62524, 52.01460, -155.43856, -132.83251), "North Pacific", "Ocean"), 2020, 0, 0.0)
region4 : RegionCondition = RegionCondition(Region(GlobeRect(35.23421, 35.31154, -120.72305, -120.61785), "SLO", "Agriculture City"), 2021, 47545, 151000.0)

example_region_conditions : List[RegionCondition] = [region1, region2, region3, region4]

#This function calculates the tons of CO2 emitted by a single person per year
def emissions_per_capita(r:RegionCondition) -> float:
    if r.pop <= 0:
        raise ValueError("Population can not be 0")
    return r.ghg_rate / r.pop

#This function calculates the area (in square kilometers) of GlobeRect
def area(gr:GlobeRect) -> float:
    y1km = gr.lo_lat * 111.32
    y2km = gr.hi_lat * 111.32
    r = 6371
    init_sa = (2 * math.pi * r * y2km) - (2 * math.pi * r * y1km)
    actual_sa = init_sa * ((abs(gr.west_long - gr.east_long)) / 360)
    return actual_sa

#This function calculates the CO2 emissions per km^2
def emissions_per_square_km(c:RegionCondition) -> float:
    if area(c.region.rect) <= 0:
        raise ValueError("Area can not be 0")
    return c.ghg_rate / area(c.region.rect)


    
# put all test cases in the "Tests" class.
class Tests(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(14,14)

    def test_epc_1(self):
        self.assertEqual(emissions_per_capita(region2), 26.54)
    def test_epc_2(self):
        self.assertEqual(emissions_per_capita(region3), ValueError)

    def test_area(self):
        self.assertEqual(area(region1.region.rect), 217.3)

if (__name__ == '__main__'):
    unittest.main()
