# What is duck typing in Python? Explain with a polymorphic function that uses duck typing.

class bird :
    def fly(self):
        return "flying high"

class airoplane:
    def fly(self):
        return "Taking off"

def flyer(fly):
    print(fly.fly())

flyer()
