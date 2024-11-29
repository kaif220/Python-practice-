# Explain method overloading and how Python simulates it with default arguments.
class math:
    def func(self,a,b,c=0):
        return a+b+c

math = math()
print(math.func(23,23,23))
print(math.func(23,23))
