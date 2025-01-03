import copy

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def deep_copy(self):
        return copy.deepcopy(self)
    
if __name__ == "__main__" :
    l1 = Line(Point(1, 2), Point(3, 4))
    l2 = l1.deep_copy()
    l2.start.x = 10
    print(l1.start.x, l2.start.x)