# 2.	Simple Arithmetic Operations
# Write a program to add, subtract, multiply, and divide two numbers.
n1 = int(input('Type a int number: '))
n2 = int(input('Type a second int number: '))
choose_operator = input('What operation do you want to do? (+, -, *, /): ')
operator = ''
result = None
if choose_operator in ('+-/*'):
    if choose_operator == '+':
        operator = '+'
        result = n1 + n2
    elif choose_operator == '-':
        operator = '-'
        result = n1 - n2
    elif choose_operator == '*':
        operator = '*'
        result = n1 * n2
    elif choose_operator == '/':
        operator = '/'
        result = n1 / n2 
else:
    print('You choosed a invalid operator.')

if result:
    print(f'{n1} {operator} {n2} = {result}')