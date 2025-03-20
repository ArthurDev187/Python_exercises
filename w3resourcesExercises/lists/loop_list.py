thislist = ["apple", "banana", "cherry"]

# You can loop through the list items by using a for loop

# for x in thislist:
#     print(x)

# Print all items by referring to their index number

# for i in range(len(thislist)):
#     print(f'{i}  {thislist[i]}')

# Print all items, using a while loop to go through all the index numbers

# i = 0
# while i < len(thislist):
#     print(thislist[i])
#     i += 1

# List Comprehension offers the shortest syntax for looping through lists

[print(x) for x in thislist]