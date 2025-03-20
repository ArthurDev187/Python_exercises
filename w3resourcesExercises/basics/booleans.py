#testing some conditions with booleans return
# print(10 > 9)
# print(5 == 5)
# print(5 == '5')
# print('st' == 'st')
# print(5.0 == 5)
# print(None == True)

# print('\n\n')

# Print a message based on whether the condition is True or False:

# a = 200
# b = 300

# if a > b:
#     print('The value of a is bigger than b')
# else:
#     print('The value of b is bigger than a')


# Evaluate Values and Variables

# print(bool('Hello'))
# print(bool(None))



# One more value, or object in this case, evaluates to False, and that is if you have 
# an object that is made from a class with a __len__ function that returns 0 or False:

class myclass():
    def __len__(self):
        return 0
    

myobj = myclass()
print(bool(myobj))