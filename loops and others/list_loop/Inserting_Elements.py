# Write a program to create a list of even numbers from 2 to 10. Use the insert() method in a loop to add the number 0 at the beginning of the list.
lst = []
n = int(input("enter a number :- "))
for item in range(1,n+1):
    if item % 2 == 0:
        lst.append(item)
print("Before Inserted List :- " ,lst)
lst.insert(0,10)
print("after inserted list :- ", lst)