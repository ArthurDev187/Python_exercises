"To add one item to a set use the add() method."

thisset = {"apple", "banana", "cherry"}
thatset = {"apple", "banana", "cherry"}
thisset.add('orange')
print(thisset)

"""To add items from another set into the current set, use the update() method.
Example
Add elements from tropical into thisset:"""

tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)

"Add elements of a list to at set:"

mylist = ["kiwi", "orange"]

thatset.update(mylist)
print(f'{thatset=}')