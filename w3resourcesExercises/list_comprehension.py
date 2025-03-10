fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

"""List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
Example:
Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
Without list comprehension you will have to write a for statement with a conditional test inside:"""

# newlist = []

# for x in fruits:
#     if "a" in x:
#         newlist.append(x)

# print(newlist)

"""With list comprehension you can do all that with only one line of code:"""

# newlist = [x for x in fruits if "a" in x]
# print(newlist)

"""Only accept items that are not "apple"""

# newlist = [x for x in fruits if x != 'apple']
# print(newlist)

"""You can use the range() function to create an iterable"""

# newlist = [x for x in range(10)]
# print(newlist)

"""Accept only numbers lower than 5"""

# newlist = [x for x in range(10) if x <= 5]
# print(newlist)

"""Set the values in the new list to upper case"""

# newlist = [x.upper() for x in fruits]
# print(newlist)

"""Set all values in the new list to 'hello'"""

# newlist = ['hello' for x in range(10)]
# print(newlist)

"""Return "orange" instead of "banana"""

newlist = [x if x != 'banana' else 'orange' for x in fruits]
print(newlist)