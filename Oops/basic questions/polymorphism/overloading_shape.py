# Create a polymorphic function that can accept different types of shapes (like Circle and Rectangle) and calculate their area.
import math

class circle :
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius **2)

class Rectangle :
    def __init__(self,length,width=1):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

shapes = [circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(shape.area())