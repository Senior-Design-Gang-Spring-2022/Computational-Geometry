from points import Point
from lines import Line_Segment
from circle import Circle
from CompGeo import CompGeo
import points as points

import random
randomx1 = 5.29
randomy1 = 3.30
point1 = Point(randomx1, randomy1)

randomx2 = 9.32
randomy2 = 14.87
point2 = Point(randomx2, randomy2)

line1 = Line_Segment(point1, point2)
circle1 = Circle(point1, 7.0)


def test_getx():
    assert point1.getx() == randomx1
    assert point2.getx() == randomx2

def test_gety():
    assert point1.gety() == randomy1
    assert point2.gety() == randomy2

def test_get_coord():
    assert point1.get_coord() == (randomx1, randomy1)
    assert point2.get_coord() == (randomx2, randomy2)

def test_get_line_segment():
    assert line1.get_line_segment() == ((randomx1, randomy1), (randomx2, randomy2))

def test_length_of_line():
    assert line1.length_of_line() == 12.25

def test_get_center():
    assert circle1.get_center() == (randomx1, randomy1)

def test_get_radius():
    assert circle1.get_radius() == 7.0

geo = CompGeo()
def test_intersect():
    assert geo.line_intersect(1,2,6,0,3,1,7,8) == (3.09302, 1.16279)
    assert geo.line_intersect(5,0,10,0,0,5,10,5) == 0
    assert geo.line_intersect(0,0,0,10,1,0,10,0) == (0,0)

# def test_distance():
#     assert geo.find_distance(2,4,0,0) == 4.47
#     assert geo.find_distance(5,9, 22, 37) == 32.76


def test_closest_point():
    # Driver code
    P = [Point(2.0, 3.0), Point(12.0, 30.0),
    Point(40.0, 50.0), Point(5.0, 1.0),
    Point(12.0, 10.0), Point(3.0, 4.0)]
    n = len(P)
    assert points.closest(P, n) == 1.4142135623730951

