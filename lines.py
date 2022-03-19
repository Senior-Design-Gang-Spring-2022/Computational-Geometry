from points import Point
class Line_Segment:
    def __init__(self, point1, point2):
        assert isinstance(point1, Point), f"{point1} is not a point."
        assert isinstance(point2, Point), f"{point2} is not a point."
        self.__point1 = point1
        self.__point2 = point2

    def get_line_segment(self):
        return (self.__point1.get_coord(), self.__point2.get_coord())

    def set_line_segment(self, point1, point2):
        assert isinstance(point1, Point), f"{point1} is not a point."
        assert isinstance(point2, Point), f"{point2} is not a point."
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
        distance = round(distance, 2)
        return distance


    def __str__(self):
        return f"({self.__point1}, {self.__point2})"
