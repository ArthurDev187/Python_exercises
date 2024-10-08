# 9.	Check Leap Year
# Write a program to check if a given year is a leap year.
print("Let's see if the year is a leap year?")
year = int(input('Type a year: '))
print()

leap = year % 4 == 0
if leap:
    print(f"{year} It's a leap year")
else:
    print(f"{year}, It's not a leap year.")
