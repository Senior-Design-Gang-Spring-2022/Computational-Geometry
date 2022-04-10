If CSV file input is chosen, the program will loop through reading each line, taking sets of two comma separated values at a time. The format looks like: 

x1,y1,x2,y2,x3,y3,x4,y4
x5,y5............,xn,yn  

If an x value is not complemented by a y value, it is dropped. 
Line segments will be formed using adjacent points. While trying to form line segments, if there is only one point, it is dropped.

If trying to use line segments or points, make sure there are an even number of values on each line, and an even number of points.  
