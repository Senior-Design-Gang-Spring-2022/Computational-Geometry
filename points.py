class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def setx(self, x):
        self.__x = x

    def gety(self):
        return self.__y

    def sety(self, y):
        self.__y = y

    def get_coord(self):
        return (self.__x, self.__y)

    def __str__(self):
        return f"({self.__x}, {self.__y})"
