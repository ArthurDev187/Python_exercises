# List objects have a sort() method that will sort the list alphanumerically, ascending, by default

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

# Sort the list alphabetically

thislist.sort()
print(thislist)

# Sort the list numerically
num_list = [100, 50, 65, 82, 23]

num_list.sort()
print(num_list)

print()

# Sort the list descending
print('List reversed')
thislist.sort(reverse=True)
print(thislist)

# sort num list descending

print()
print('Num list, descending.')
num_list.sort(reverse=True)
print(num_list)

print()
print()

# Case sensitive sorting can give an unexpected result

thatlist = ["banana", "Orange", "Kiwi", "cherry"]
thatlist.sort(key = str.lower)
print(thatlist)