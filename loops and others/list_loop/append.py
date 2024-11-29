# write a program to initiate an empty list and use for loop to append the number from 1 to 10 to the list use the append() method

lst = []
n = int(input("enter a number between 1 to 10 : ")) 
for item in range(1,n+1):
    lst.append(item)
print(lst)
