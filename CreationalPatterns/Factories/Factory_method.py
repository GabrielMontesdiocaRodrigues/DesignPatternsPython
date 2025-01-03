
from enum import Enum
from math import cos, sin

class CoordinatesSystem(Enum) :
    CARTESIAN = 1
    POLAR = 2

class Point :
    def __init__(self, x, y) :
        self.x = x
        self.y = y

    #! What we dont want is to have a constructor with a lot of parameters
    # def __init__(self, a, b, system = CoordinatesSystem.CARTESIAN) :
    #     if system == CoordinatesSystem.CARTESIAN:
    #         self.x = a
    #         self.y = b
    #         
    #     elif system == CoordinatesSystem.POLAR:
    #         self.x = a * cos(b)
    #         self.y = a * sin(b)
    

    @staticmethod
    def new_cartesian_point(x, y) :
        return Point(x, y)
    
    @staticmethod
    def new_polar_point(rho, theta) :
        return Point(rho * cos(theta), rho * sin(theta))
    
    def __str__(self) :
        return f'x: {self.x}, y: {self.y}'

if __name__ == "__main__" :
    p1 = Point.new_cartesian_point(1, 2)
    p2 = Point.new_polar_point(3, 4)
    print(p1)
    print(p2)