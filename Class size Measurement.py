import math
class Square: #class
    def __init__(self, side):
        self.side=side
    def area(self):
        return self.side**2
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area (self):
        return math.pi*(self.radius**2) # Area formula: π * r^2
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def __str__ (self):
        return f'rect with {self.length} and {self.width}'
    def area (self):
        return self.width*self.length
s1=Square(4)
print ("Area of the Square=",s1.area())
c1=Circle(5)
print ( "Area of the Circle=",c1.area())
r1=Rectangle(5,6)
print ( "Area of the Rectangle=",r1.area())
