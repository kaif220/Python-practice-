# Write a program to create a list of characters from 'a' to 'j'. Use a loop to remove every second element from the list using the pop() method and print the updated list.

characters = []
for i in range(97,106):
    characters.append(chr(i))
    
print(characters)


