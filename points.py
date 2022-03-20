class Point:
    def __init__(self, x, y):
        assert isinstance(x,float), f"Entered value of x: {x} is not a float"
        assert isinstance(y,float), f"Entered value of x: {y} is not a float"
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def setx(self, x):
        assert isinstance(x,float), f"Entered value of x: {x} is not a float"
        self.__x = x

    def gety(self):
        return self.__y

    def sety(self, y):
        assert isinstance(y,float), f"Entered value of x: {y} is not a float"
        self.__y = y

    def get_coord(self):
        return (self.__x, self.__y)

    def __str__(self):
        return f"({self.__x}, {self.__y})"
