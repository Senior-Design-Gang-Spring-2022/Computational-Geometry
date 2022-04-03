from points import Point
from lines import Line_Segment
from circle import Circle
from line_intersection import Line_Segment_Intersection
from convex_hull import ConvexHull
from closest_points import ClosestPoints

import points as points
import main as main
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
    assert line1.length_of_line() == 12.25177

def test_get_center():
    assert circle1.get_center() == (randomx1, randomy1)

def test_get_radius():
    assert circle1.get_radius() == 7.0

# geo = CompGeo()
def test_intersect():
    x1 = 1.0
    x2 = 2.0
    point1 = Point(x1,x2)
    x3 = 6.0
    x4 = 0.0
    point2 = Point(x3,x4)
    line1 = Line_Segment(point1, point2)

    x5 = 3.0
    x6 = 1.0
    point3 = Point(x5,x6)
    x7 = 7.0
    x8 = 8.0
    point4 = Point(x7,x8)
    line2 = Line_Segment(point3, point4)
    line_intersection = Line_Segment_Intersection()
    assert line_intersection.line_intersect(line1,line2).getx() == 3.09302
    assert line_intersection.line_intersect(line1,line2).gety() == 1.16279

    x1 = 5.0
    x2 = 0.0
    point1 = Point(x1,x2)
    x3 = 10.0
    x4 = 0.0
    point2 = Point(x3,x4)
    line1 = Line_Segment(point1, point2)

    x5 = 0.0
    x6 = 5.0
    point3 = Point(x5,x6)
    x7 = 10.0
    x8 = 5.0
    point4 = Point(x7,x8)
    line2 = Line_Segment(point3, point4)
    assert line_intersection.line_intersect(line1,line2) == '-'

    x1 = 0.0
    x2 = 0.0
    point1 = Point(x1,x2)
    x3 = 0.0
    x4 = 10.0
    point2 = Point(x3,x4)
    line1 = Line_Segment(point1, point2)

    x5 = 1.0
    x6 = 0.0
    point3 = Point(x5,x6)
    x7 = 10.0
    x8 = 0.0
    point4 = Point(x7,x8)
    line2 = Line_Segment(point3, point4)
    #line_intersection = Line_Segment_Intersection()
    assert line_intersection.line_intersect(line1,line2) == '-'

# def test_brute_force():
#     P = [Point(2.0, 3.0), Point(12.0, 30.0),Point(40.0, 50.0), Point(5.0, 1.0),
#     Point(12.0, 10.0), Point(3.0, 4.0)]
#     n = 6
#     cp = ClosestPoints()
#     assert cp.bruteForce(P, n) == 3.60555

def test_brute_force_invalid_arguments(): 
    P3 = [Point(2.0, 3.0)]
    n3 = 1
    cp3 = ClosestPoints()
    assert cp3.bruteForce(P3,n3) == None

    P2 = [Point(2.0,3.0), Point(12.0,30.0), Point(40.0, 50.0)]
    n2 = 2
    assert cp.bruteForce(P2, n2) == -1

def test_closest_point():
    P = [Point(2.0, 3.0)]
    n = len(P)
    cp3 = ClosestPoints()
    assert isinstance(cp, ClosestPoints)
    assert cp.closest(P, n) == 1.41421


def test_convex_hull():
    convex_hull = ConvexHull()
    assert isinstance(convex_hull, ConvexHull)

    points = []
    points.append(Point(0.0, 3.0))
    points.append(Point(2.0, 2.0))
    points.append(Point(1.0, 1.0))
    points.append(Point(2.0, 1.0))
    points.append(Point(3.0, 0.0))
    points.append(Point(0.0, 0.0))
    points.append(Point(3.0, 3.0))
    for elem in points: 
        assert isinstance(elem, Point)
    ch = ConvexHull()
    assert ch.convexHull(points, len(points)) == [0.0, 3.0, 0.0, 0.0, 3.0, 0.0, 3.0, 3.0]


    
    