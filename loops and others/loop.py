# n = int(input("Enter Any Value : "))
    
# for i in range (1,n+1):
#     for j in range(i):
#         print(i , end= " ")
    
#     print()

# n = int(input("enter any value : "))  # Size of the square
# for i in range(n):
#     for j in range(i):
#         if i==0 or i == 1 or i==n-1 or i == n - 2 or j == 0 or j==1 or j==n-1 or j == n - 2:
#             print( "K" , end=' ')  # Print stars for the border
#         else:
#             print(' ', end=' ')  # Print spaces for the inner part
#     print()  # Move to the next line after each row

#  for item in range(int(input("enter ith values :- "))):
#     for j in range (int(input("Enter Jth iteration value  : "))):
#         print("$",end=" ")
#     print()
# n=int(input("enter a value in this"))
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(' ', end="")
#     for k in range(i):
#             print("*" ,end="")
#     print()
# n = int(input("enter any value : "))  # Size of the square
# for i in range(n):
#     for j in range(i):
#         if j==0 or j == 1 or i==n:
#             print( "K" , end=' ')  # Print stars for the border
#         else:
#             print(' ', end=' ')  # Print spaces for the inner part
#     print()
my_list = [("data", 12), ("sql", 13), ("python", 4), ("javascript", 20)]

    # make into [{word:"data", count:12},
    #            {word:"sql", count:13},
    #            {word:"python", count:4}...etc]

final_list = []
my_dict = {}



for s in my_list:
    my_dict["word"] = s[0]
    my_dict["count"] = s[1]

    final_list.append(my_dict)

print(final_list)
