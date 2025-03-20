"""Join Sets
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.

Union
The union() method returns a new set with all items from both sets.

Example
Join set1 and set2 into a new set:
"""

set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}

# set3 = set1.union(set2)
# print(f'{set3=}')

"You can use the | operator instead of the union() method, and you will get the same result."

set3 = set1 | set2
print(f'{set3=}')

"""Join Multiple Sets
All the joining methods and operators can be used to join multiple sets.

When using a method, just add more sets in the parentheses, separated by commas:

Example
Join multiple sets with the union() method:"""

set4 = {'f', 'g', 'h', 'i'}
set5 = {5, 6, 7, 8, 9}

set1 = set1.union(set3, set4, set5)
print(f'{set1=}')

"""Join a Set and a Tuple
The union() method allows you to join a set with other data types, like lists or tuples.

The result will be a set.

Example
Join a set with a tuple:"""

mylist = list([True, None, False, 1, 43.1, 'list'])
print(F'{mylist=}\n')
set6 = set4.union(set5, mylist)
print(f'{set6=}')