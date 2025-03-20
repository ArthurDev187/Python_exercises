thistuple = ('apple', 'banana', 'kiwi')
print(thistuple)

"""Tuple Items
Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

Allow Duplicates
Since tuples are indexed, they can have items with the same value:"""

duplicatedtuple = ('Banana', 'cherry', 'banana', 'cherry', 'orange')
print(duplicatedtuple)

"""Tuple Length
To determine how many items a tuple has, use the len() function:"""

print(len(thistuple))
print()

# One item tuple, remember the comma:

its_a_tuple = ('Apple',)
its_not_a_tuple = ('Apple')
print(f'{its_a_tuple=} {type(its_a_tuple)}')
print(f'{its_not_a_tuple=} {type(its_not_a_tuple)}\n')


"""Tuple items can be of any data type:
Example
String, int and boolean data types:"""


print(f'Tuples types accepted')
stringtuple = ('apple', 'pinapple', 'orange')
numbertuple = (1, 2, 3, 4, 5.0)
booltuple = (True, True, False, False)
print(f'{stringtuple=}')
print(f'{numbertuple=}')
print(f'{booltuple=}')

# A tuple with strings, integers and boolean values:

mixtuple = (123, 'tuple', True, '342', 432.2, None)
print(f'{mixtuple=}')

# Using the tuple() method to make a tuple:

tuplemethod = tuple((1234, 4312.2, 'abcd', True))
print(f'{tuplemethod=}')