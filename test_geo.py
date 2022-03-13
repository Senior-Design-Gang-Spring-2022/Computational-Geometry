def line_intersect(x1,y1,x2,y2,x3,y3,x4,y4): 
    D = ((x1-x2)*(y3-y4) - ((y1-y2) * (x3 - x4)))
    if (D == 0): 
        print("Lines are parallel")
        return 0
    Px = ((((x1*y2)-(y1*x2)) * (x3-x4))-((x1-x2)*((x3*y4)-(y3*x4))))/D
    Py = ((((x1*y2)-(y1*x2))*(y3-y4)) -((y1-y2)*(x3*y4 - y3 *x4)))/D
    return round(Px, 5), round(Py, 5)

def test_intersect(): 
    assert line_intersect(1,2,6,0,3,1,7,8) == (3.09302, 1.16279)
    assert line_intersect(5,0,10,0,0,5,10,5) == 0
    assert line_intersect(0,0,0,10,1,0,10,0) == (0,0)
 
