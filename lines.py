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

    def __str__(self):
        return f"({self.__point1}, {self.__point2})"
