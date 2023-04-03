# Exercise 01: Create a function with variable length of arguments
"""
Write a program to create function func1() to accept a variable length of arguments and print their value.
Note: Create a function in such a way that we can pass any number of arguments to this function, and the function should process them and display each argument’s value.

Function call:

# call function with 3 arguments
func1(20, 40, 60)

# call function with 2 arguments
func1(80, 100)
Expected Output:

Printing values
20
40
60

Printing values
80
100
"""
def func1(*args):
    for i in args:
        print(i)

func1(20, 40, 60)
func1(80, 100)


# Exercise 02: Create an inner function to calculate the addition in the following way
"""
Create an outer function that will accept two parameters, a and b
Create an inner function inside an outer function that will calculate the addition of a and b
At last, an outer function will add 5 into addition and return it
"""
# outer function
def outer_fun(a, b):
    square = a ** 2

    # inner function
    def addition(a, b):
        return a + b

    # call inner function from outer function
    add = addition(a, b)
    # add 5 to the result
    return add + 5

result = outer_fun(5, 10)
print(result)


# Exercise 03: Create a function with a default argument
"""
Write a program to create a function show_employee() using the following conditions.
It should accept the employee’s name and salary and display both.
If the salary is missing in the function call then assign default value 9000 to salary

Given:
showEmployee("Ben", 12000)
showEmployee("Jessa")

Expected output:
Name: Ben salary: 12000
Name: Jessa salary: 9000
"""
# function with default argument
def show_employee(name, salary=9000):
    print("Name:", name, "salary:", salary)

show_employee("Ben", 12000)
show_employee("Jessa")


# Exercise 6: Create a recursive function
"""
Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
HINT:A recursive function is a function that calls itself again and again.

Expected Output:
55
"""
def addition(num):
    if num:
        # call same function by reducing number by 1
        return num + addition(num - 1)
    else:
        return 0

res = addition(10)
print(res)

