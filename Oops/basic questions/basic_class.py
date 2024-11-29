class student:
    def __init__(self,name,age,addresh):  # declare the constructot __init__.
        self.name = "Mohammad Kaif Qureshi"
        self.age = 24
        self.addresh = "Fatehpur Sikri Agra :"

a = student("name","age","addresh")
print(a.name)
print(a.age)
print(a.addresh)
print(type(a))