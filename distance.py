from math import sqrt

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff = abs(self.x - other.x)
        y_diff = abs(self.y - other.y)
        return sqrt((x_diff**2) + (y_diff**2))
    
    def __repr__(self):
        return f'Point({self.x}, {self.y})'
    
    
c1 = Point(2,3)
c2 = Point(5,6)

c1.distance(c2)
