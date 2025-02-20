# 13.	Factorial Calculation
# Write a program to compute the factorial of a number.

number = int(input('Type a number to see the factorial: ')) 
total = 1
for i in range(number, 1, -1):
    total *= i 

print(f'Factorial: {total}')