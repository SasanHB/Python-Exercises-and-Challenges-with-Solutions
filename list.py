# Exercise 01: Concatenate two lists in the following order
"""
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

Expected output:
['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
"""
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

res = [x + y for x in list1 for y in list2]
print(res)


# Exercise 02: Iterate both lists simultaneously
"""
Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.

Given
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

Expected output:
10 400
20 300
30 200
40 100
"""
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)


# Exercise 03: Remove all occurrences of a specific item from a list.
"""
Given a Python list, write a program to remove all occurrences of item 20.

Given:
list1 = [5, 20, 15, 20, 25, 50, 20]

Expected output:
[5, 15, 25, 50]
"""
# Solution 01
list1 = [5, 20, 15, 20, 25, 50, 20]

# list comprehension
# remove specific items and return a new list
def remove_value(sample_list, val):
    return [i for i in sample_list if i != val]

res = remove_value(list1, 20)
print(res)

# Solution 02
list1 = [5, 20, 15, 20, 25, 50, 20]

while 20 in list1:
    list1.remove(20)
print(list1)