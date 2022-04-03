from points import Point
from lines import Line_Segment
from circle import Circle
from line_intersection import Line_Segment_Intersection
from convex_hull import ConvexHull
import copy

# milestones
# get rid main.py & separate all of these functions into its own class
# redo most of the tests, place an emphasis onto test-driven development
# for each function 
#  - pythonfile with the class function
#  - pythonfile with the tests/asserts

# Driver Code
points = []
points.append(Point(0.0, 3.0))
points.append(Point(2.0, 2.0))
points.append(Point(1.0, 1.0))
points.append(Point(2.0, 1.0))
points.append(Point(3.0, 0.0))
points.append(Point(0.0, 0.0))
points.append(Point(3.0, 3.0))
 
print("Convex Hull/ Coordinates of smallest convex polygon:")
# found = convexHull(points, len(points))
print("-")

