# Exercise 01: Convert two lists into a dictionary
"""
Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

Expected output:
{'Ten': 10, 'Twenty': 20, 'Thirty': 30}
"""
# Solution 01
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# empty dictionary
res_dict = dict()

for i in range(len(keys)):
    res_dict.update({keys[i]: values[i]})
print(res_dict)

# Solution 02
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

res_dict = dict(zip(keys, values))
print(res_dict)

# Merge two Python dictionaries into one??


# Exercise 02: Create a dictionary by extracting the keys from a given dictionary
"""
Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

Given dictionary:
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
# Keys to extract
keys = ["name", "salary"]

Expected output:
{'name': 'Kelly', 'salary': 8000}
"""
# Solution 01
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# keys to extract
keys = ["name", "salary"]

# new dict
res = dict()

for k in keys:
    # add current key with its va;ue from sample_dict
    res.update({k: sample_dict[k]})
print(res)


# Solution 02
sampleDict = { 
  "name": "Kelly",
  "age":25, 
  "salary": 8000, 
  "city": "New york" }

keys = ["name", "salary"]

newDict = {k: sampleDict[k] for k in keys}
print(newDict)


# Exercise 03: Delete a list of keys from a dictionary
"""
Given:
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys to remove
keys = ["name", "salary"]

Expected output:
{'city': 'New york', 'age': 25}
"""
# Solution 01
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys to remove
keys = ["name", "salary"]

for k in keys:
    sample_dict.pop(k)
print(sample_dict)

# Solution 02
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys to remove
keys = ["name", "salary"]

sample_dict = {k: sample_dict[k] for k in sample_dict.keys() - keys}
print(sample_dict)


# Exercise 04: Rename key of a dictionary
"""
Write a program to rename a key city to a location in the following dictionary.

Given:
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

Expected output:
{'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}
"""