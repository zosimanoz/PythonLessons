'''
In Python, a function is a group of related statements that performs a specific task.

Functions help break our program into smaller and modular chunks. As our program grows larger and larger, functions make it more organized and manageable.

Furthermore, it avoids repetition and makes the code reusable.
'''


def function_name(parameters):
	"""docstring"""
	statement(s)


def add(x, y):
    return x + y

s = add(a, b)
m = add(c, d)
c = add(x, y)


# TYPES OF FUNCTIONS
# Built-in functions - Functions that are built into Python.
# User-defined functions - Functions defined by the users themselves.


# Function Definition
def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")


# Function call
greet('Ramesh')

'''
Note: In python, the function definition should always be present before the function call. 
Otherwise, we will get an error. For example,
'''


'''
The first string after the function header is called the docstring and is short for documentation string. 
It is briefly used to explain what a function does.
'''

print(greet.__doc__)

'''
In the above example, we have a docstring immediately below the function header. We generally use triple quotes so that docstring can extend up to multiple lines. 
This string is available to us as the __doc__ attribute of the function.
'''

'''
The return statement is used to exit a function and go back to the place from where it was called.
'''

def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >= 0:
        return num
    else:
        return -num


print(absolute_value(2))

print(absolute_value(-4))





# BUILT-IN FUNCTIONS

# abs function
number = -20

absolute_number = abs(number)
print(absolute_number)


# filter function: extracts elements from an iterable (list, tuple etc.) for which a function returns True
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# returns True if number is even
def check_even(number):
    if number % 2 == 0:
          return True  

    return False

# Extract elements from the numbers list for which check_even() returns True
even_numbers_iterator = filter(check_even, numbers)

# converting to list
even_numbers = list(even_numbers_iterator)

print(even_numbers)

# Output: [2, 4, 6, 8, 10]



## FUNCTION ARGUMENTS
def greet(name, msg):
    """This function greets to
    the person with the provided message"""
    print("Hello", name + ', ' + msg)

greet("Monica", "Good morning!")

""" if we dont pass argument, it will give error. """

"""
Variable Function Arguments
"""

# 1. Python Default Arguments

def greet(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """

    print("Hello", name + ', ' + msg)


greet("Kate")
greet("Bruce", "How do you do?")


""" Any number of arguments in a function can have a default value. But once we have a default argument,
 all the arguments to its right must also have default values.

non-default arguments cannot follow default arguments.
"""

# def greet(msg = "Good morning!", name): 
    # will result in error


"""
Python allows functions to be called using keyword arguments. 
When we call functions in this way, the order (position) of the arguments can be changed. 
Following calls to the above function are all valid and produce the same result.
"""

# 2 keyword arguments
greet(name = "Bruce",msg = "How do you do?")

# 2 keyword arguments (out of order)
greet(msg = "How do you do?",name = "Bruce") 

# 1 positional, 1 keyword argument
greet("Bruce", msg = "How do you do?")   

# Having a positional argument after keyword arguments will result in errors.
# greet(name="Bruce","How do you do?")


"""
Python Arbitrary Arguments: *args, **kwargs
*args: Non Keyword Arguments
**kwargs: Keyword Arguments
"""


def adder(x,y,z):
    print("sum:",x+y+z)

adder(10,12,13)

# Lets see what happens when we pass more than 3 arguments in the adder() function.

def adder(x,y,z):
    print("sum:",x+y+z)

adder(5,10,15,20,25)

# In Python, we can pass a variable number of arguments to a function using special symbols: *args, *kwargs

"""
Python has *args which allow us to pass the variable number of non keyword arguments to function.

1. Using *args to pass the variable length arguments to the function (Pass parameters as tuple)

"""

def adder(*num):
    sum = 0
    
    for n in num:
        sum = sum + n

    print("Sum:",sum)

adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)


"""
Python passes variable length non keyword argument to function using *args but we cannot use this to pass keyword argument. 
For this problem Python has got a solution called **kwargs, it allows us to pass the variable length of keyword arguments 
to the function. (Pass parameters as dictionary)

"""

def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="Ram", Lastname="Prasad", Email="ram@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)