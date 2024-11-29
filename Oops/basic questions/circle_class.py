# Q4. Create a Circle class with a method to calculate its area given the radius.
import math
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi * (self.radius**2)
    
areas = circle(8)
print(areas.area())