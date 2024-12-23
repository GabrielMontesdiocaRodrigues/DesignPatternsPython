class Rectangle : 
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width  

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height 

    @height.setter
    def height(self, value):  
        self._height = value

    def area(self):
        return self._width * self._height   
    
    def __str__(self):
        return f'Width: {self._width}, height: {self._height}'

# This is a violation of the Liskov Substitution Principle
class Square(Rectangle) : 
    def __init__(self, size):
        Rectangle.__init__(self, size, size)
    
    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value

def use_it(rc): 
    w = rc.width
    rc.height = 10
    expected = w*10
    print(f'Expected an area of {expected}, got {rc.area()}')


if __name__ == '__main__':
    rc = Rectangle(2, 3)
    use_it(rc)

    sq = Square(5)
    use_it(sq)