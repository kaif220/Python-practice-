listy = []

user = int(input('enter a number'))

for i in range (user):
    item = int(input("enter a values : "))
    listy.append(item)
    
print(listy)
print(listy.pop())