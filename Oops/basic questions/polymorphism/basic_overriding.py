# Q1. What is polymorphism? Write a simple example to demonstrate polymorphism.
class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

def animal_sound(animal):
    print(animal.sound())

animal_sound(Dog())  # Output: Bark
animal_sound(Cat())  # Output: Meow
# Here, both Dog and Cat classes have a sound method, and animal_sound demonstrates polymorphism by calling sound on different types of objects.