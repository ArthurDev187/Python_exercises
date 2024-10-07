from math import pi
# 7.	Area of a Circle
# Write a program to calculate the area of a circle from a given radius.

print('We are going to calculate the area of a Circle from a given radius.')
radius = float(input('Type the radius: '))
area = pi * (radius**2)
print(f'The area of the circle: {area:.2f}')
