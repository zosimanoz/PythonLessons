import module
import math

sum = module.add(3,4)
print(f"Sum from module: {sum}")


# import statement example
# to import standard module math

print("pi:", math.pi)


"""
Importing by renaming
"""
import math as m
print("The value of pi is", m.pi)


"""
Python from...import statement:
We can import specific names from a module without importing the module as a whole.
"""

# import only pi from math module
from math import pi, e
print("The value of pi only method included: ", pi)
print("The value of e only method included: ", e)


"""
Importing all names:
We can import all names(definitions) from a module using the following construct:
Importing everything with the asterisk (*) symbol is not a good programming practice. 
This can lead to duplicate definitions for an identifier. It also hampers the readability of our code.
"""
# import all names from the standard module math

from math import *
print("The value of pi is", pi)


