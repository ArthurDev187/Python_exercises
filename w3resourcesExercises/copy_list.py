
"""You cannot copy a list simply by typing list2 = list1, because: list2 will only 
be a reference to list1, and changes made in list1 will automatically also be made in list2.
You can use the built-in List method copy() to copy a list."""

thislist = ["apple", "banana", "cherry"]

# Make a copy of a list with the copy() method:

mylist = thislist.copy()
mylist[0] = 'orange'
print(f'{thislist=}')
print(f'{mylist=}')


# Another way to make a copy is to use the built-in method list().

mysecondlist = list(thislist)
mysecondlist[1] = 'açaí'
print(f'{mysecondlist=}')

# Make a copy of a list with the : operator:

mythirdlist = thislist[:]
mythirdlist[2] = 'pinaple'
print(f'{mythirdlist=}')
