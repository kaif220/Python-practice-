# print only even number from list

lst  =  [1,2,3,4,5,6,7,8,9]
even_list =[]
for item in lst:
    if item % 2 == 0 :
        even_list.append(item)
print(even_list)

# another method 

lst = [1, 2, 3, 4, 5, 6]
for elem in lst:
    if elem % 2 == 0:
        print(elem)
