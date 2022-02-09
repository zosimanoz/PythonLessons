
'''
Python has the following data types built-in by default, in these categories:

Text Type: 	str
Numeric Types: 	int, float, complex
Sequence Types: 	list, tuple, range
Mapping Type: 	dict
Set Types: 	set
Boolean Type: 	bool
Binary Types: 	bytes, bytearray
'''

x = "Hello World" 	#str 	
x = 20 	#int 	
x = 20.5 	#float 	
x = 1j 	#complex 	
x = ["apple", "banana", "cherry"] 	#list 	
x = ("apple", "banana", "cherry") 	#tuple 	
x = range(6) 	#range 	
x = {"name" : "John", "age" : 36} 	#dict 	
x = {"apple", "banana", "cherry"} 	#set 	
x = frozenset({"apple", "banana", "cherry"}) 	#frozenset 	
x = True 	#bool 	
x = b"Hello" 	#bytes 	
x = bytearray(5) 	#bytearray 	
x = memoryview(bytes(5)) #memoryview



x = str("Hello World") 	#str 	
x = int(20) 	#int 	
x = float(20.5) 	#float 	
x = complex(1j) 	#complex 	
x = list(("apple", "banana", "cherry")) 	#list 	
x = tuple(("apple", "banana", "cherry")) 	#tuple 	
x = range(6) 	#range 	
x = dict(name="John", age=36) 	#dict 	
x = set(("apple", "banana", "cherry")) 	#set 	
x = frozenset(("apple", "banana", "cherry")) 	#frozenset 	
x = bool(5) 	#bool 	
x = bytes(5) 	#bytes 	
x = bytearray(5) 	#bytearray 	
x = memoryview(bytes(5)) 	#memoryview



'''
Python Numbers
'''

x = 1    # int
y = 2.8  # float
z = 1j   # complex


x = 35e3
y = 12E4
z = -87.7e100

print(x)
print(y)
print(z)


'''
Random Numbers:

Python does not have a random() function to make a random number, 
but Python has a built-in module called random that can be used to make random numbers:
'''

import random
print(random.randrange(1, 10)) #display random number between 1 and 9


'''
The random number generator needs a number to start with (a seed value), 
to be able to generate a random number.
By default the random number generator uses the current system time.

'''
# the generator creates a random number based on the seed value, 
# so if the seed value is 10, you will always get 0.5714025946899135 as the first random number.

import random
random.seed(10)
print(random.random())

# if you use same seed twice, you get same random number twice
import random
random.seed(10)
print(random.random())

random.seed(11)
print(random.random())


'''
random.choice() return random element from a list
'''

import random
mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist)) 


'''
random.choices(sequence, weights=None, cum_weights=None, k=1):
The choices() method returns a list with the randomly selected element from the specified sequence.
You can weigh the possibility of each result with the weights parameter or the cum_weights parameter.
The sequence can be a string, a range, a list, a tuple or any other kind of sequence.
'''

import random
mylist = ["apple", "banana", "cherry"]
print(random.choices(mylist, weights = [10, 1, 1], k = 14)) 


'''
There may be times when you want to specify a type on to a variable. 
This can be done with casting. Python is an object-orientated language, 
and as such it uses classes to define data types, including its primitive types.
'''

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0' 