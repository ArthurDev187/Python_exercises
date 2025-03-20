"""Update
The update() method inserts all items from one set into another.

The update() changes the original set, and does not return a new set.

Example
The update() method inserts the items in set2 into set1:"""

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}

# set1.update(set2)
# print(f'{set1=}')

"""Intersection
Keep ONLY the duplicates

The intersection() method will return a new set, that only contains the items that are present in both sets.

Example
Join set1 and set2, but keep only the duplicates:"""

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.intersection(set2)
# print(F'{set3=}')

"""You can use the & operator instead of the intersection() method, and you will get the same result.

Example
Use & to join two sets:"""

# set3 = set1 & set2
# print(F'{set3}')


"""The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

Example
Keep the items that exist in both set1, and set2:"""

# set1.intersection_update(set2)
# print(f'{set1=}')

"""The values True and 1 are considered the same value. The same goes for False and 0.
Example
Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:
"""
# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}

# set3 = set1.intersection(set2)
# print(f'{set3=}')

"""Difference
The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

Example
Keep all items from set1 that are not in set2:"""

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

# set3 = set1.difference(set2)
# print(f'{set3}')

"""Symmetric Differences
The symmetric_difference() method will keep only the elements that are NOT present in both sets.

Example
Keep the items that are not present in both sets:"""

set3 = set1.symmetric_difference(set2)
print(f'{set3=}')