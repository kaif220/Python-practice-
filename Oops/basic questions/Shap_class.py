#Q2.Create a Rectangle class with attributes length and width, and a method to calculate the area.

class rectangle:
    def __init__(self,length,width):
        self.length= length 
        self.width= width
    def area(self):
        
        return "the area of rectangle is : ", self.length * self.width

areas = rectangle(7,10)
print(areas.area())
