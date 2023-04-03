#Exercise 01: Count all letters, digits, and special symbols from a given string
"""
Given:
str1 = "P@#yn26at^&i5ve"

Expected Outcome:
Total counts of chars, digits, and symbols 
Chars = 8 
Digits = 3 
Symbol = 4
"""
def find_digits_chars_symbols(sample_str):
    char_count = 0
    digit_count = 0
    symbol_count = 0
    for char in sample_str:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        # if it is not letter or digit then it is special symbol
        else:
            symbol_count += 1

    print("Chars =", char_count, "Digits =", digit_count, "Symbol =", symbol_count)

sample_str = "P@yn2at&#i5ve"
print("total counts of chars, Digits, and symbols \n")
find_digits_chars_symbols(sample_str)

# Exercise 02: Create a mixed String using the following rules
"""
Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.

Given:
s1 = "Abc"
s2 = "Xyz"

Expected Output:
AzbycX
"""
s1 = "Abc"
s2 = "Xyz"

# get string length
s1_length = len(s1)
s2_length = len(s2)

# get length of a bigger string
length = s1_length if s1_length > s2_length else s2_length
result = ""

# reverse s2
s2 = s2[::-1]

# iterate string 
# s1 ascending and s2 descending
for i in range(length):
    if i < s1_length:
        result = result + s1[i]
    if i < s2_length:
        result = result + s2[i]

print(result)

# Exercise 03: String characters balance Test
"""
Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter.

Given:

Case 1:
s1 = "Yn"
s2 = "PYnative"
Expected Output:
True

Case 2:
s1 = "Ynf"
s2 = "PYnative"
Expected Output:
False
"""
def string_balance_test(s1, s2):
    flag = True
    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
    return flag


s1 = "Yn"
s2 = "PYnative"
flag = string_balance_test(s1, s2)
print("s1 and s2 are balanced:", flag)

s1 = "Ynf"
s2 = "PYnative"
flag = string_balance_test(s1, s2)
print("s1 and s2 are balanced:", flag)


# Exercise 04: Write a program to count occurrences of all characters within a string
"""
Given:
str1 = "Apple"

Expected Outcome:
{'A': 1, 'p': 2, 'l': 1, 'e': 1}
"""
str1 = "Apple"

# create a result dictionary
char_dict = dict()

for char in str1:
    count = str1.count(char)
    # add / update the count of a character
    char_dict[char] = count
print('Result:', char_dict)


# Exercise 05: Find the last position of a given substring
"""
Write a program to find the last position of a substring “Emma” in a given string.

Given:
str1 = "Emma is a data scientist who knows Python. Emma works at google."

Expected Output:
Last occurrence of Emma starts at index 43
"""
str1 = "Emma is a data scientist who knows Python. Emma works at google."
print("Original String is:", str1)

index = str1.rfind("Emma")
print("Last occurrence of Emma starts at index:", index)


# Exercise 06: Remove special symbols / punctuation from a string
"""
Given:
str1 = "/*Jon is @developer & musician"

Expected Output:
"Jon is developer musician"
"""
# Solution 01
import string

str1 = "/*Jon is @developer & musician"
print("Original string is ", str1)

new_str = str1.translate(str.maketrans('', '', string.punctuation))

print("New string is ", new_str)

#Solution 02
import re

str1 = "/*Jon is @developer & musician"
print("Original string is ", str1)

# replace special symbols with ''
res = re.sub(r'[^\w\s]', '', str1)
print("New string is ", res)

