# Given two straight line segments( represented as a start point and an end point), compute the point of intersection, if any.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setLocation(self, x, y):
        self.x = x
        self.y = y

    
class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        deltaX = self.end.x - self.start.x
        deltaY = self.end.y - self.start.y
        self.slope = deltaX / deltaY
        self.yintercept = end.y - (self.slope * self.end.x)

def swap(pointA, pointB):
    x,y = pointA.x,pointA.y
    pointA.setLocation(pointB.x, pointB.y)
    pointB.setLocation(x,y)

def isBetween(start, middle, end):
    if start > end:
        return end <= middle and middle <= start
    else :
        return start <= middle and middle <= end

def isBetweenPoint(start, middle, end):
    return isBetween(start.x,middle.x, end.x) and isBetween(start.y, middle.y, end.y)

def intersection(start1, end1, start2, end2):

    if start1.x > end1.x : swap(start1,end1)
    if start2.x > end2.x : swap(start2,end2)
    if start1.x > start2.x :
        swap(start1,start2)
        swap(end1,end2)

    line1 = Line(start1, end1)
    line2 = Line(start2, end2)


    if line1.slope == line2.slope:
        if line1.yintercept == line2.yintercept and isBetweenPoint(start1,start2, end1):
            return start2
        return None
    
    interceptX = (line2.yintercept - line1.yintercept) / (line1.slope - line2.slope)
    interceptY = (interceptX * line1.slope) + line1.yintercept

    intersectionPoint = Point(interceptX, interceptY)

    if isBetweenPoint(start1,intersectionPoint,end1) and isBetweenPoint(start2,intersectionPoint, end2):
        return intersectionPoint

    return None

pointResult = intersection(Point(0,0), Point(10,10),Point(0,10), Point(10,0))
print(pointResult.x, pointResult.y)