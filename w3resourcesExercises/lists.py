this_list = ['Banana', 'Apple', 'Cherry', 'Apple', 'Cherry', 7384, 43.4, True]
# print(len(this_list))
# print(type(this_list))

# print()
# another_list = list(('list', 'blackberry', 1234, False))
# print(another_list)
# print(type(another_list))


print(this_list[4])
print(this_list[-1])
print(this_list[-7])
print(this_list[3:7])
print(this_list[2:-2])
print(this_list[::2])
print(this_list[::-2])
print()

if 'Apple' in this_list:
    print('Apple is in the list.')
else:
    print('Apple is not in the list.')