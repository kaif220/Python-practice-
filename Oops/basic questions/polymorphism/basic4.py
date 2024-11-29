#Q4. Create a superclass Shape with a method area, and subclass Square that overrides area to demonstrate polymorphism.
class shape:
    def area(self):
        return 0
class square(shape):
    def __init__(self,sq):
        self.sq = sq
    def area(self):
        return self.sq * self.sq
square = square(6)
print(square.area())

