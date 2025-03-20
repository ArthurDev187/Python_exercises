# Write a Python program to find a list of integers with exactly two occurrences 
# of nineteen and at least three occurrences of five. Return True otherwise False.
list_int = [14, 15, 5, 3, 5, 5, 5, 5, 5, 2]
nineteen = False
count_five = 0
for i in list_int:
    if i == 19:
        nineteen = True
    elif i == 5:
        count_five += 1

result = (f'{nineteen=}, {count_five=}')
print(result)
print()
if nineteen and count_five > 2:
    print('The list has nineteen and 3 or more numbers 5.')
else:
    print('The list has not the necessary to pass.')
# teste
print()