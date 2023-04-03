# Exercise 01: Display float number with 2 decimal places using print()
"""
Given:
num = 458.541315

Expected Output:
458.54
"""
num = 458.541315
print('%.2f' % num)

# Exercise 02: Write all content of a given file into a new file by skipping line number 5
"""
Given test.txt file:
line1
line2
line3
line4
line5
line6
line7

Expected Output: new_file.txt
line1
line2
line3
line4
line6
line7
"""
# read test.txt
with open("test.txt", "r") as fp:
    # read all lines from a file
    lines = fp.readlines()

# open new file in write mode
with open("new_file.txt", "w") as fp:
    count = 0
    # iterate each lines from a test.txt
    for line in lines:
        # skip 5th lines
        if count == 4:
            count += 1
            continue
        else:
            # write current line
            fp.write(line)
        # in each iteration reduce the count
        count += 1


# Exercise 03: Format variables using a string.format() method.
"""
Write a program to use string.format() method to format the following three variables as per the expected output

Given:
totalMoney = 1000
quantity = 3
price = 450

Expected Output:
I have 1000 dollars so I can buy 3 football for 450.00 dollars.
"""
quantity = 3
totalMoney = 1000
price = 450
statement1 = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars."
print(statement1.format(quantity, totalMoney, price))
