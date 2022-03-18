from points import Point
class Circle:
    def __init__(self, center, radius):
        assert isinstance(center, Point), f"Provided {center} is not a point."
        assert isinstance(radius, float), f"Given {radius} is not a float type."
        self.__center = center
        self.__radius = radius

    def set_center(self, center):
        assert isinstance(center, Point), f"{center} is not a point."
        self.__center = center

    def set_radius(self, radius):
        assert isinstance(radius, float), f"{radius} is not a float type."
        self.__radius = radius

    def get_center(self):
        return self.__center.get_coord()

    def get_radius(self):
        return self.__radius

    def __str__(self):
        return f"Center:{self.__center.get_coord()}, Radius: {self.__radius}"
