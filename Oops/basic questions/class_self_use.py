# Create a simple person class with arguments with attribute name and age , and method to display them.
class person: # define class
    def __init__(self,name,age): # using constructor make attribute for object 
        self.name=name # self is a keyword It's used in class methods to access attributes and methods of the instance the method is called on. Let's break down why self is essential:
        self.age= age
    def display(self): # method it means working on attributes for object in class
        print(f"name : {self.name} , Age : {self.age}" )

vars= person("Kaif" , 23)
vars.display()
