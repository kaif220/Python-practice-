# Initialize a list of numbers from 1 to 10. Use a for loop to iterate over the list and remove all odd numbers using the remove() method.

lst = [1,2,3,4,5,6,7,8,9,10]

for item in lst : 
    if item % 2 != 0 :
        lst.remove(item)

print(lst)