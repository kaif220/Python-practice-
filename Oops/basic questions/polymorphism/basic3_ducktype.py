# Demonstrate polymorphism by creating a function that works with multiple types of objects (using duck typing).
class Car:
    def start(self):
        return "Car started"

class Bike:
    def start(self):
        return "Bike started"

def start_vehicle(vehicle):
    print(vehicle.start())

start_vehicle(Car())  # Output: Car started
start_vehicle(Bike()) # Output: Bike started
