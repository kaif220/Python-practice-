# Q5. Write a Python program that demonstrates polymorphism with a method speak in two classes Person and Robot.
class human :
    def sound(self):
        return "hello i am human ! "

class robot:
    def sound(self):
        return "beeep jzz xhhh shsuoahdu"
    

def conversation(entity):
    print(entity.sound())


conversation(human())
conversation(robot())