"""Accessing Items
You can access the items of a dictionary by referring to its key name, inside square brackets:

Example
Get the value of the "model" key:
There is also a method called get() that will give you the same result:
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict['model']
y = thisdict.get('model')
print(x)
print(y)

"The keys() method will return a list of all the keys in the dictionary."
"Add a new item to the original dictionary, and see that the keys list gets updated as well:"

thisdict['color'] = 'red'

z = thisdict.keys()
print(z)


"The values() method will return a list of all the values in the dictionary."

a = thisdict.items()
print(a)

"Make a change in the original dictionary, and see that the items list gets updated as well:"

thisdict['year'] = '2020'
print(a)

"""Check if Key Exists
To determine if a specified key is present in a dictionary use the in keyword:"""

print('model' in thisdict)
