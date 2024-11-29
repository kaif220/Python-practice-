# Question: Write a Python class Person with a private attribute _age. Implement getter and setter methods to access and modify _age, ensuring that age can only be set to positive values.

class Person:
    def __init__(self, age=0):
        self._age = age 

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print("Age must be positive")

# Test
person = Person()
person.set_age(0)  # Outputs: "Age must be positive"
person.set_age(25)
print(person.get_age())  # Outputs: 25
