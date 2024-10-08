# 11.	Sum of List
# Write a program to calculate the sum of all elements in a list.
new_list = [
    1, 1, 1, 1, 'fdsa', '2'
]
total_sum = 0

for i in new_list:
    if i.isnumeric():
        total_sum += float(i)

print(f'Total sum elements in the list: {total_sum}')