"""To remove an item in a set, use the remove(), or the discard() method.
Example
Remove "banana" by using the remove() method:"""

thisset = {"apple", "banana", "cherry"}

# thisset.remove('banana')
# print(thisset)

"Remove 'banana' by using the discard() method:"

# thisset.discard('banana')
# print(thisset)


"""You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

The return value of the pop() method is the removed item.

Example
Remove a random item by using the pop() method:"""

# x = thisset.pop()
# y = thisset.pop()

# print(x)
# print(y)

"The del keyword will delete the set completely:"

del thisset

print(thisset)
