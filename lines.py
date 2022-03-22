from points import Point
class Line_Segment:
    def __init__(self, point1, point2):
        assert isinstance(point1, Point), "The entered datatype is not a point."
        assert isinstance(point2, Point), "The entered datatype is not a point."
        self.__point1 = point1
        self.__point2 = point2

    def get_line_segment(self):
        return (self.__point1.get_coord(), self.__point2.get_coord())

    def set_line_segment(self, point1, point2):
        assert isinstance(point1, Point), "The entered datatype is not a point."
        assert isinstance(point2, Point), "The entered datatype is not a point."
        self.__point1 = point1
        self.__point2 = point2

    def length_of_line(self):
        x1 = self.__point1.getx()
        y1 = self.__point1.gety()
        x2 = self.__point2.getx()
        y2 = self.__point2.gety()
        part1 = (x2-x1)**2.0
        part2 = (y2-y1)**2.0
        addition = part1 + part2
        half = 1.0/2.0
        distance = addition**half
        distance = round(distance, 5)
        return distance

    #https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
    def onSegment(self, another_point):
        '''
        Check if another_point is in the line.
        '''
        assert isinstance(another_point, Point), "The entered datatype is not a point."
        x1 = self.__point1.getx()
        y1 = self.__point1.gety()
        x2 = self.__point2.getx()
        y2 = self.__point2.gety()
        x3 = another_point.getx()
        y3 = another_point.gety()

        if ( (x3 <= max(x1, x2)) and (x3 >= min(x1, x2)) and (y3 <= max(y1, y2)) and (y3 >= min(y1, y2))):
            return True
        return False

    def orientation(self, another_point):
        assert isinstance(another_point, Point), "The entered datatype is not a point."
        x1 = self.__point1.getx() #p.x
        y1 = self.__point1.gety() #p.y
        x2 = self.__point2.getx() #r.x
        y2 = self.__point2.gety() #r.y
        x3 = another_point.getx() #q.x
        y3 = another_point.gety() #q.y

        val = (float(y3 - y1) * (x2 - x3)) - (float(x3 - x1) * (y2 - y3))
        if (val > 0.0): #clockwise orientation
            return 1.0
        elif (val < 0.0): #counterclockwise orientation
            return 2.0
        else:
            return 0.0 #colinnear



    def __str__(self):
        return f"({self.__point1}, {self.__point2})"
