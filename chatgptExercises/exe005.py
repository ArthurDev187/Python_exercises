# 5.	Fahrenheit to Celsius
# Write a program to convert temperatures from Fahrenheit to Celsius.
print('Lets convert from F° to C°')
f = int(input('type temperature in F°: '))

c = (f - 32) * (5/9) 
print(f'Temperature: C°{c:.0f}')