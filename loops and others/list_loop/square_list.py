# create a square of a list 

lst = [1,2,3,4]
new_list = []

for item in lst :
    sqr = item *item 
    new_list.append(sqr)
print(new_list)

## another method

lst = [1, 2, 3, 4]
squares = []
for elem in lst:
    squares.append(elem ** 2)
print(squares)
