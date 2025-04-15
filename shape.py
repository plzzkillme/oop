class Shape:
  def area(self):
    pass
  def get_area(self,area):
    print(Circle.area(),Square.area())
class Circle(Shape):
  def __init__(self,radius):
    self.radius=radius
  def area(self):
    print(3.14*radius**2)
class Square(Shape):
    def __init__(self,length,width):
      self.length=length
      self.wiidth=width
  def area(self):
    print(length*width)
  
