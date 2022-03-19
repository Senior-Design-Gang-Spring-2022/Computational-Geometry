from points import Point
from lines import Line_Segment
from circle import Circle

point1 = Point(9.0,8.0)
point2 = Point(5.0,6.0)

print(point1)
print(point2)

line1 = Line_Segment(point1,point2)
print(line1)
print(line1.length_of_line())

circle1 = Circle(point1, 7.0)
print(circle1)
