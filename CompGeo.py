import math
class CompGeo():

    def line_intersect(x1,y1,x2,y2,x3,y3,x4,y4): 
        D = ((x1-x2)*(y3-y4) - ((y1-y2) * (x3 - x4)))
        if (D == 0): 
            print("Lines are parallel")
            return 0
        Px = ((((x1*y2)-(y1*x2)) * (x3-x4))-((x1-x2)*((x3*y4)-(y3*x4))))/D
        Py = ((((x1*y2)-(y1*x2))*(y3-y4)) -((y1-y2)*(x3*y4 - y3 *x4)))/D
        return round(Px, 5), round(Py, 5)

    ##finding the distance between two pairs of coordinates
    def find_distance(p1x, p1y, p2x, p2y):
        return round(math.sqrt((p1x - p2x)**2 + (p1y - p2y)**2), 2)

def test_distance():
    assert CompGeo.find_distance(2,4,0,0) == 4.47