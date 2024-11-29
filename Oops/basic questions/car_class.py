# Q5. Create a Car class with an attribute speed and a method to increase speed.
class car:
    def __init__(self,name,model,speed=0):
        self.name = name
        self.model = model
        self.speed = speed 
    def accelerate(self,increase):
        self.speed += increase
    def display_speed(self):
        print(f"the name of car : {self.name} \n model of car : {self.model}\n speed of car : {self.speed}")

cars = car("Fortuner","toyota")
cars.accelerate(30)
cars.display_speed()