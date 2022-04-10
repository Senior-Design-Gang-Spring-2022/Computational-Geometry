from points import Point
from lines import Line_Segment

class Line_Segment_Intersection:
  def checkIntersect(self, line1, line2):
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
  def line_intersect(self, line1,line2):
      assert isinstance(line1, Line_Segment), "The entered datatype is not a Line."
      assert isinstance(line2, Line_Segment), "The entered datatype is not a Line."
      if self.checkIntersect(line1,line2) == False:
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

p1 = Point(1.0, 1.0)
q1 = Point(10.0, 1.0)
p2 = Point(1.0, 2.0)
q2 = Point(10.0, 2.0)

line1 = Line_Segment(p1,q1)
line2 = Line_Segment(p2,q2)
line_intersection = Line_Segment_Intersection()
print(line_intersection.line_intersect(line1,line2))

p1 = Point(10.0, 0.0)
q1 = Point(0.0, 10.0)
p2 = Point(0.0, 0.0)
q2 = Point(10.0,10.0)

line1 = Line_Segment(p1,q1)
line2 = Line_Segment(p2,q2)
print(line_intersection.line_intersect(line1,line2))


p1 = Point(-5.0,-5.0)
q1 = Point(0.0, 0.0)
p2 = Point(1.0, 1.0)
q2 = Point(10.0, 10.0)

line1 = Line_Segment(p1,q1)
line2 = Line_Segment(p2,q2)
print(line_intersection.line_intersect(line1,line2))
