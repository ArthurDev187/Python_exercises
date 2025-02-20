# 6.	Find Largest Number
# Write a program that finds the largest of three numbers.
n1 = int(input('Type n1: ')) 
n2 = int(input('Type n2: '))
n3 = int(input('Type n3: '))
result = None
if n1 == n2 == n3:
    print('Os números são iguais.')
else:
    if n1 > n2 and n1 > n3:
        result = n1
    elif n2 > n1 and n2 > n3:
        result = n2
    elif n3 > n1 and n3 > n2:
        result = n3
    print(f'O maior número é: {result}')