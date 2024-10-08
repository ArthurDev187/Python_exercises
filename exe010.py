# 10.	Count Vowels in a String
# Write a program to count the number of vowels in a string.
print("Let's count the vowels.")
word = str(input('Type a word or a sentence: '))
counting_vowels = 0
vowels = 'AEIOU' 
for i in word:
    if i.upper in vowels:
        counting_vowels += 1

print()
print(f'({word}) has {counting_vowels} vowels.')
