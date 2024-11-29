# Create a program that initializes a list with some numbers. Use a loop to generate a list of their squares, and then add these squares to the original list using the extend() method.

lst = [1,2,3,5,6]
new_lst = []
for item in lst : 
    sqr = item * item
    new_lst.append(sqr)
print(new_lst)
lst.extend(new_lst)
print(lst)