"""But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
Example
Unpacking a tuple:"""


"""
If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
Example
Add a list of values the "tropic" variable:"""

fruits = ('apple', 'banana', 'orange', 'strawberry', 'raspberry')
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
