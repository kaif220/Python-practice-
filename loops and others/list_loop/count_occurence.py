# count occurence of an element :

# lst = [1,1,1,2,3,4,4,6,7,7]
lst = [1, 2, 3, 2, 4, 2]
target = 2
count = 0
for elem in lst:
    if elem == target:
        count += 1
print("Count of", target, ":", count)

# another method 

lst1 = [1,1,1,2,2,5,3,3,0,0,4,4,5,7,7,8,8,9,9,10]
number = int(input('enter any number : '))


if number <  0:
        print("enter a positive number ")
else :
    count = 0
    for item in lst1:
        if item == number : 

            count = count + 1 
    
        
    print("count of " , number , ": ", count)