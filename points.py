import math
import copy

class Point:
    def __init__(self, x, y):
        assert isinstance(x,float), "Entered value of x is not a float"
        assert isinstance(y,float), "Entered value of y is not a float"
        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def setx(self, x):
        assert isinstance(x,float), "Entered value of x is not a float"
        self.x = x

    def gety(self):
        return self.y

    def sety(self, y):
        assert isinstance(y,float), "Entered value of y is not a float"
        self.y = y

    def get_coord(self):
        return (self.x, self.y)

    # def __str__(self):
    #     return f'({self.x}, {self.y})'
