from points import Point

c = Point(3, 5)

def test_getx():
    assert c.getx() == 3

def test_gety():
    assert c.gety() == 5

def test_get_coord():
    assert c.get_coord() == (3, 5)

