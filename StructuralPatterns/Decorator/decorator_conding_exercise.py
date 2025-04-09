class Circle:
  def __init__(self, radius):
    self.radius = radius

  def resize(self, factor):
    self.radius *= factor

  def __str__(self):
    return f'circle of radius {self.radius}'

class Square:
  def __init__(self, side):
    self.side = side

  def __str__(self):
    return f'square with side {self.side}'


class ColoredShape:
  def __init__(self, shape, color):
    self.color = color
    self.shape = shape

  def resize(self, factor):
    if isinstance(self.shape, Circle):
      self.shape.resize(factor)

  def __str__(self):
    return f'A {self.shape} has the color {self.color}'