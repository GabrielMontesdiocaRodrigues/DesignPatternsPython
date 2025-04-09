from abc import ABC

class Shape(ABC): 
    def __str__(self): 
        return ''
    
class Circle(Shape): 
    def __init__(self, radius): 
        self.radius = radius
    
    def resize(self, fastor):
        self.radius *= fastor
    
    def __str__(self): 
        return f'Circle of radius {self.radius}'
    
class Square(Shape): 
    def __init__(self, side): 
        self.side = side

    def __str__(self):
        return f'Square with side {self.side}'
    
class ColoredShape(Shape): 
    def __init__(self, shape, color): 
        if isinstance(shape, ColoredShape): 
            raise Exception('Decorated shape cannot be decorated')

        self.shape = shape
        self.color = color
    
    def __str__(self):
        return f'{self.shape} of color {self.color}'
    
class TransparentShape(Shape):
    def __init__(self, shape, transparency):
        self.shape = shape
        self.transparency = transparency

    def __str__(self):
        return f'{self.shape} with transparency {self.transparency*100.0}%'

if __name__ == '__main__':
    circle = Circle(10)
    print(circle)
    
    red_circle = ColoredShape(circle, 'red')
    print(red_circle)
    red_half_transparent_circle = TransparentShape(red_circle, 0.5)
    print(red_half_transparent_circle)

    mixed = ColoredShape(ColoredShape(Square(20), 'red'), 'blue')
    print(mixed)