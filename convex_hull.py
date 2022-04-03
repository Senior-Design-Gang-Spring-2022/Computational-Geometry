
class ConvexHull:
    def Left_index(self, points):
        '''
        Finding the left most point
        '''
        minn = 0
        for i in range(1,len(points)):
            if points[i].x < points[minn].x:
                minn = i
            elif points[i].x == points[minn].x:
                if points[i].y > points[minn].y:
                    minn = i
        return minn
    
    def orientation(self, p, q, r):
        '''
        To find orientation of ordered triplet (p, q, r).
        The function returns following values
        0 --> p, q and r are collinear
        1 --> Clockwise
        2 --> Counterclockwise
        '''
        val = (q.y - p.y) * (r.x - q.x) - \
            (q.x - p.x) * (r.y - q.y)
    
        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2
    
    def convexHull(self, points, n):
        
        # There must be at least 3 points
        if n < 3:
            return
    
        # Find the leftmost point
        l = self.Left_index(points)
    
        hull = []
        found = [] 
        '''
        Start from leftmost point, keep moving counterclockwise
        until reach the start point again. This loop runs O(h)
        times where h is number of points in result or output.
        '''
        p = l
        q = 0
        while(True):
            
            # Add current point to result
            hull.append(p)
    
            '''
            Search for a point 'q' such that orientation(p, q,
            x) is counterclockwise for all points 'x'. The idea
            is to keep track of last visited most counterclock-
            wise point in q. If any point 'i' is more counterclock-
            wise than q, then update q.
            '''
            q = (p + 1) % n
    
            for i in range(n):
                
                # If i is more counterclockwise
                # than current q, then update q
                if(self.orientation(points[p],
                            points[i], points[q]) == 2):
                    q = i
    
            '''
            Now q is the most counterclockwise with respect to p
            Set p as q for next iteration, so that q is added to
            result 'hull'
            '''
            p = q
    
            # While we don't come to first point
            if(p == l):
                break
    
        # Print Result
        for each in hull:
            print("x: ", points[each].x, "y: ",  points[each].y)
            ## storing the coordinates for test
            found.append(points[each].x)
            found.append(points[each].y)

        return found