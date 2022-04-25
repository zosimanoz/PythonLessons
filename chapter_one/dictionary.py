"""
Python dictionary is an unordered collection of items. Each item of a dictionary has a key/value pair.
Creating a dictionary is as simple as placing items inside curly braces {} separated by commas.
An item has a key and a corresponding value that is expressed as a pair (key: value).
"""

# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1:'apple', 2:'ball'})

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])


"""
Accessing Elements from Dictionary

While indexing is used with other data types to access values, a dictionary uses keys. 
Keys can be used either inside square brackets [] or with the get() method.
"""

# get vs [] for retrieving elements
my_dict = {'name': 'Jack', 'age': 26}

# Output: Jack
print(my_dict['name'])

# Output: 26
print(my_dict.get('age'))

# Trying to access keys which doesn't exist throws error
# Output None
print(my_dict.get('address'))

# KeyError
print(my_dict['address'])


"""
Changing and Adding Dictionary elements

Dictionaries are mutable. We can add new items or change the value of existing items using an assignment operator.
"""

# Changing and adding Dictionary Elements
my_dict = {'name': 'Jack', 'age': 26}

# update value
my_dict['age'] = 27

#Output: {'age': 27, 'name': 'Jack'}
print(my_dict)

# add item
my_dict['address'] = 'Downtown'

# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
print(my_dict)


"""
Removing elements from Dictionary

We can remove a particular item in a dictionary by using the pop() method.
This method removes an item with the provided key and returns the value.

All the items can be removed at once, using the clear() method

We can also use the del keyword to remove individual items or the entire dictionary itself.
"""

# Removing elements from a dictionary

# create a dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# remove a particular item, returns its value
# Output: 16
print(squares.pop(4))

# Output: {1: 1, 2: 4, 3: 9, 5: 25}
print(squares)

# remove an arbitrary item, return (key,value)
# Output: (5, 25)
print(squares.popitem())

# Output: {1: 1, 2: 4, 3: 9}
print(squares)

# remove all items
squares.clear()

# Output: {}
print(squares)

# delete the dictionary itself
del squares

# Throws Error
print(squares)



"""
Accessing dictionary items: 
"""

for item in squares.items():
    print(item)

for k, v in squares.items():
    print(f"key: {k}, val: {v}")


"""
Python Dictionary Comprehension
Dictionary comprehension is an elegant and concise way to create a new dictionary from an iterable in Python.
"""

# Dictionary Comprehension
squares = {x: x*x for x in range(6)}

print(squares)

# This code is equivalent to:

squares = {}
for x in range(6):
    squares[x] = x*x
print(squares)


# Dictionary Comprehension with if conditional
odd_squares = {x: x*x for x in range(11) if x % 2 == 1}

print(odd_squares)