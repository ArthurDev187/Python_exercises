"Python Dictionaries"

thisdict = {
    "brand" : "Ford", 
    "model" : "Mustang",
    "year" : "1964",
    "year" : "2020"
}

"""Dictionary
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
Dictionaries are written with curly brackets, and have keys and values:"""

print(F'{thisdict=}, \nThisdict type: {type(thisdict)}\n')

"""Dictionary items are ordered, changeable, and do not allow duplicates.
Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
Example
Print the "brand" value of the dictionary:"""

print(thisdict['brand'])
print(thisdict['year'])

"""Dictionary Length
To determine how many items a dictionary has, use the len() function:

Example
Print the number of items in the dictionary:"""
print(len(thisdict))

"""Dictionary Items - Data Types
The values in dictionary items can be of any data type:

Example
String, int, boolean, and list data types:"""
thisdict['electric'] = True
thisdict['colors'] = ['black', 'blue', 'red', 'yellow', 'orange']
print(thisdict)

"""The dict() Constructor
It is also possible to use the dict() constructor to make a dictionary.

Example
Using the dict() method to make a dictionary:"""

thatdict = dict(name = 'Arthur', age = 30, nationality = 'Brazilian')
print(f'{thatdict=}')
print(f'Type: {type(thatdict)}')