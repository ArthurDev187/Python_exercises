"""Join Two Lists
There are several ways to join, or concatenate, two or more lists in Python.
One of the easiest ways are by using the + operator."""

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list3 = list1 + list2
print(f'{list3=}')
print()

#Another way to join two lists is by appending all the items from list2 into list1, one by one:

list4 = ['d', 'e', 'f']
list5 = [4, 5, 6]

for x in list5:
    list4.append(x)

print(f'{list4=}\n')


# Or you can use the extend() method, where the purpose is to add elements from one list to another list:

list6 = ['g', 'h', 'j']
list7 = [7, 8, 9]
list6.extend(list7)

print(f'{list6=}')