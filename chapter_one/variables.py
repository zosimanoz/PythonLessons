
'''
Variables are containers for storing data values.
Python has no command for declaring a variable.
'''

x = 5
y = "Manoj"
print(x)
print(y)



'''
Variables do not need to be declared with any particular type, and can even change type after they have been set.
'''
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x) 

'''
use type(variable_name) function to know the type of variables
'''
print(type(x))

'''
Type casting: If you want to specify the data type of a variable, this can be done with casting.
'''
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 

print(type(x))
print(type(y))
print(type(z))


'''
NOTE: Variable names are case sensitive
'''
a = 4
A = "Sally"
# A will not overwrite a 
print('a and A are different')


'''
 Rules for Python variables:
    A variable name must start with a letter or the underscore character
    A variable name cannot start with a number
    A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    Variable names are case-sensitive (age, Age and AGE are three different variables)
'''

# Legal variable names: 

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


# Illegal variable names:

# 2myvar = "John"
# my-var = "John"
# my var = "John"

'''
Python allows you to assign values to multiple variables in one line:
'''

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

'''
And you can assign the same value to multiple variables in one line:
'''

x = y = z = "Mango"
print(x)
print(y)
print(z)


'''
If you have a collection of values in a list, tuple etc. 
Python allows you extract the values into variables. This is called unpacking.
'''

fruits = ["orange", "banana", "papaya"]
x, y, z = fruits
print(x)
print(y)
print(z)

'''
The Python print() statement is often used to output variables.
To combine both text and a variable, Python uses the + character:
'''
x = "awesome"
print("Python is " + x)


'''
Concatenating two variables
'''
x = "Python is "
y = "awesome"
z =  x + y
print(z)


'''
+ works as addition for numeric variables
'''
x = 5
y = 10
print(x + y)

'''
Guess the output !
'''
# x = 5
# y = "Ram"
# print(x + y)

'''
Variables that are created outside of a function (as in all of the examples above) are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.
'''

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc() 


'''
If you create a variable with the same name inside a function, this variable will be local, 
and can only be used inside the function. The global variable with the same name will remain as it was, 
global and with the original value.
'''

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()
print("Python is " + x) 


'''
To create a global variable inside a function, you can use the global keyword.
'''

def myfunc():
  global x
  x = "fantastic"

myfunc()
print("Python is " + x) 


'''
To change the value of a global variable inside a function, refer to the variable by using the global keyword:
'''
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()
print("Python is " + x) 

