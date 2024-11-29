#How does method overriding achieve polymorphism in Python? Write a simple example with a superclass and a subclass.

class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

animal = Animal()
dog = Dog()
print(animal.sound())  # Output: Some sound
print(dog.sound())     # Output: Bark
