from points import Point
from lines import Line_Segment
from circle import Circle

import random
randomx1 = random.randint(-1000,1000)
randomy1 = random.randint(-1000,1000)
point1 = Point(randomx1, randomy1)

randomx2 = random.randint(-1000,1000)
randomy2 = random.randint(-1000,1000)
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

def test_get_center():
    assert circle1.get_center() == (randomx1, randomy1)

def test_get_radius():
    assert circle1.get_radius() == 7.0
