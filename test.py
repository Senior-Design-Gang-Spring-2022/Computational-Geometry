from points import Point
from CompGeo import CompGeo

c = Point(3, 5)

def test_getx():
    assert c.getx() == 3

def test_gety():
    assert c.gety() == 5

def test_get_coord():
    assert c.get_coord() == (3, 5)

aayush
print("Random Changes")
def test_intersect(): 
    assert CompGeo.line_intersect(1,2,6,0,3,1,7,8) == (3.09302, 1.16279)
    assert CompGeo.line_intersect(5,0,10,0,0,5,10,5) == 0
    assert CompGeo.line_intersect(0,0,0,10,1,0,10,0) == (0,0)
    
main
