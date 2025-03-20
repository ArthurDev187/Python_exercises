thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thistuple = ("kiwi", "orange")
#using append method

# thislist.append('orange')
# print(thislist)

#using inset method

# thislist.insert(1, 'orange')
# print(thislist)

# using extend method

# thislist.extend(tropical)
# print(thislist)

# Add elements of a tuple to a list

thislist.extend(thistuple)
print(thislist)
print(type(thislist))