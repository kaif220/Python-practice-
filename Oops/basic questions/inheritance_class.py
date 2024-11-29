#Q8. Create an Animal base class with a method speak, and two subclasses Dog and Cat that override speak.

class animal:
    def speak(self):
        print("wow sound")
class dog(animal):
    def speak(self):
        print("bark....")

class cat(animal):
    def speak(self):
        print("meow....")
dog = dog() 
cat = cat()

dog.speak()
cat.speak()

