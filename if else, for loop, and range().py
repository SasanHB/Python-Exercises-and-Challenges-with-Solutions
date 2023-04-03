# Exercise 01: Display numbers from a list using loop
"""
Write a program to display only those numbers from a list that satisfy the following conditions

-The number must be divisible by five
-If the number is greater than 150, then skip it and move to the next number
-If the number is greater than 500, then stop the loop

Given:
numbers = [12, 75, 150, 180, 145, 525, 50]

Expected output:
75
150
145
"""

numbers = [12, 75, 150, 180, 145, 525, 50]
# iterate each item of a list
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    # check if number is divisible by 5
    elif item % 5 == 0:
        print(item)

# Exercise 02: Write a program to display all prime numbers within a range
"""
Note: A Prime Number is a number that cannot be made by multiplying other whole numbers. A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers

Examples:
6 is not a prime mumber because it can be made by 2×3 = 6
37 is a prime number because no other whole numbers multiply together to make it.

Given:
# range
start = 25
end = 50

Expected output:
Prime numbers between 25 and 50 are:
29
31
37
41
43
47
"""
start = 25
end = 50
print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    # all prime numbers are greater than 1
    # if number is less than or equal to 1, it is not prime
    if num > 1:
        for i in range(2, num):
            # check for factors
            if (num % i) == 0:
                # not a prime number so break inner loop and
                # look for next number
                break
        else:
            print(num)

# Exercise 03: Reverse a given integer number
"""
Given:
76542

Expected output:
24567
"""
num = 76542
reverse_number = 0
print("Given Number ", num)
while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
print("Revere Number ", reverse_number)