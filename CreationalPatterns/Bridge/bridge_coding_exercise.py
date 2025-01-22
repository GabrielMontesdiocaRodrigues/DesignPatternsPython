from abc import ABC, abstractmethod

class Renderer(ABC):
    @abstractmethod
    def __str__(self):
        raise NotImplementedError
    
class VectorRenderer(Renderer):
    def __str__(self, shape_name):
        return f'Drawing {shape_name} as lines'

class RasterRenderer(Renderer):
    def __str__(self, shape_name):
        return f'Drawing {shape_name} as pixels'

class Shape:
    def __init__(self, renderer: Renderer):
        self.name = None
        self.renderer : Renderer= renderer

    def __str__(self):
        return self.renderer.__str__(self.name)

class Triangle(Shape):
    def __init__(self, renderer: Renderer):
        super().__init__(renderer)
        self.name = 'Triangle'

class Square(Shape):
    def __init__(self, renderer: Renderer):
        super().__init__(renderer)
        self.name = 'Square'