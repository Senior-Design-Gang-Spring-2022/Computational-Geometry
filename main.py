from points import Point
from lines import Line_Segment
from circle import Circle
import copy

# The main function that returns true if
# the line segment 'p1q1' and 'p2q2' intersect.
def checkIntersect(line1, line2):
    assert isinstance(line1, Line_Segment), "The entered datatype is not a Line."
    assert isinstance(line2, Line_Segment), "The entered datatype is not a Line."
    # Find the 4 orientations required for
    # the general and special cases
    first_line = line1.get_line_segment()
    p1 = Point(first_line[0][0], first_line[0][1])
    q1 = Point(first_line[1][0], first_line[1][1])

    second_line = line2.get_line_segment()
    p2 = Point(second_line[0][0], second_line[0][1])
    q2 = Point(second_line[1][0], second_line[1][1])

    o1 = line1.orientation(p2)
    o2 = line1.orientation(q2)
    o3 = line2.orientation(p1)
    o4 = line2.orientation(q1)

    # General case
    if ((o1 != o2) and (o3 != o4)):
        return True

    # Special Cases

    # p1 , q1 and p2 are collinear and p2 lies on segment p1q1
    if ((o1 == 0.0) and line1.onSegment(p2)):
        return True

    # p1 , q1 and q2 are collinear and q2 lies on segment p1q1
    if ((o2 == 0.0) and line1.onSegment(q2)):
        return True

    # p2 , q2 and p1 are collinear and p1 lies on segment p2q2
    if ((o3 == 0.0) and line2.onSegment(p1)):
        return True

    # p2 , q2 and q1 are collinear and q1 lies on segment p2q2
    if ((o4 == 0.0) and line2.onSegment(q1)):
        return True

    # If none of the cases
    return False
#def line_intersect(self, x1,y1,x2,y2,x3,y3,x4,y4):
#def line_intersect(self, point1,point2,point3,point4):
def line_intersect(line1,line2):
    assert isinstance(line1, Line_Segment), "The entered datatype is not a Line."
    assert isinstance(line2, Line_Segment), "The entered datatype is not a Line."
    if checkIntersect(line1,line2) == False:
        return '-'

    first_line = line1.get_line_segment()
    p1 = Point(first_line[0][0], first_line[0][1])
    x1 = p1.getx()
    y1 = p1.gety()

    q1 = Point(first_line[1][0], first_line[1][1])
    x2 = q1.getx()
    y2 = q1.gety()

    second_line = line2.get_line_segment()
    p2 = Point(second_line[0][0], second_line[0][1])
    x3 = p2.getx()
    y3 = p2.gety()

    q2 = Point(second_line[1][0], second_line[1][1])
    x4 = q2.getx()
    y4 = q2.gety()

    D = ((x1-x2)*(y3-y4) - ((y1-y2) * (x3 - x4)))
    if (D == 0):
        print("Lines are parallel")
        return 0
    Px = ((((x1*y2)-(y1*x2)) * (x3-x4))-((x1-x2)*((x3*y4)-(y3*x4))))/D
    Py = ((((x1*y2)-(y1*x2))*(y3-y4)) -((y1-y2)*(x3*y4 - y3 *x4)))/D
    x_final = round(Px, 5)
    y_final = round(Py, 5)
    intersection = Point(x_final,y_final)
    return intersection

########!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# A Brute Force method to return the
# smallest distance between two points
# in P[] of size n
def bruteForce(P, n):
    min_val = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            line1 = Line_Segment(P[i], P[j])
            if line1.length_of_line() < min_val:
                min_val = line1.length_of_line()

    return min_val

# A utility function to find the
# distance between the closest points of
# strip of given size. All points in
# strip[] are sorted according to
# y coordinate. They all have an upper
# bound on minimum distance as d.
# Note that this method seems to be
# a O(n^2) method, but it's a O(n)
# method as the inner loop runs at most 6 times
def stripClosest(strip, size, d):

    # Initialize the minimum distance as d
    min_val = d


    # Pick all points one by one and
    # try the next points till the difference
    # between y coordinates is smaller than d.
    # This is a proven fact that this loop
    # runs at most 6 times
    for i in range(size):
        j = i + 1
        while j < size and (strip[j].y -
                            strip[i].y) < min_val:
            line1 = Line_Segment(strip[i], strip[j])
            min_val = line1.length_of_line()
            j += 1

    return min_val

# A recursive function to find the
# smallest distance. The array P contains
# all points sorted according to x coordinate
def closestUtil(P, Q, n):

    # If there are 2 or 3 points,
    # then use brute force
    if n <= 3:
        return bruteForce(P, n)

    # Find the middle point
    mid = n // 2
    midPoint = P[mid]

    #keep a copy of left and right branch
    Pl = P[:mid]
    Pr = P[mid:]

    # Consider the vertical line passing
    # through the middle point calculate
    # the smallest distance dl on left
    # of middle point and dr on right side
    dl = closestUtil(Pl, Q, mid)
    dr = closestUtil(Pr, Q, n - mid)

    # Find the smaller of two distances
    d = min(dl, dr)

    # Build an array strip[] that contains
    # points close (closer than d)
    # to the line passing through the middle point
    stripP = []
    stripQ = []
    lr = Pl + Pr
    for i in range(n):
        if abs(lr[i].x - midPoint.x) < d:
            stripP.append(lr[i])
        if abs(Q[i].x - midPoint.x) < d:
            stripQ.append(Q[i])

    stripP.sort(key = lambda point: point.y) #<-- REQUIRED
    min_a = min(d, stripClosest(stripP, len(stripP), d))
    min_b = min(d, stripClosest(stripQ, len(stripQ), d))


    # Find the self.closest points in strip.
    # Return the minimum of d and self.closest
    # distance is strip[]
    return min(min_a,min_b)

# The main function that finds
# the smallest distance.
# This method mainly uses closestUtil()
def closest(P, n):
    P.sort(key = lambda point: point.x)
    Q = copy.deepcopy(P)
    Q.sort(key = lambda point: point.y)

    # Use recursive function closestUtil()
    # to find the smallest distance
    return closestUtil(P, Q, n)

########!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Driver program to test above functions:
p1 = Point(1.0, 1.0)
q1 = Point(10.0, 1.0)
p2 = Point(1.0, 2.0)
q2 = Point(10.0, 2.0)

line1 = Line_Segment(p1,q1)
line2 = Line_Segment(p2,q2)
print(line_intersect(line1,line2))

p1 = Point(10.0, 0.0)
q1 = Point(0.0, 10.0)
p2 = Point(0.0, 0.0)
q2 = Point(10.0,10.0)

line1 = Line_Segment(p1,q1)
line2 = Line_Segment(p2,q2)
print(line_intersect(line1,line2))


p1 = Point(-5.0,-5.0)
q1 = Point(0.0, 0.0)
p2 = Point(1.0, 1.0)
q2 = Point(10.0, 10.0)

line1 = Line_Segment(p1,q1)
line2 = Line_Segment(p2,q2)
print(line_intersect(line1,line2))



# This code is contributed by Ansh Riyal
