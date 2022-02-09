# loop through list

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# loop through string
for x in "banana":
  print(x)


# With the break statement we can stop the loop before 
# it has looped through all the items
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


# With the continue statement we can stop the 
# current iteration of the loop, and continue with the next
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


# The range() function returns a sequence of numbers, 
# starting from 0 by default, and increments by 1 
# (by default), and ends at a specified number.
for x in range(6):
  print(x)

# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: 
# range(2, 6), which means values from 2 to 6 (but not including 6)
for x in range(2, 6):
  print(x)


# The range() function defaults to increment the sequence by 1, 
# however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3)
for x in range(2, 30, 3):
  print(x)

# We can use else in for loop
for x in range(6):
  print(x)
else:
  print("Finally finished!") 


# Nested loops
# The "inner loop" will be executed one time for each iteration of the "outer loop"
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) 


# pass statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, 
# put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass


# WHILE Loop
count = 0
while (count < 3):   
    count = count + 1
    print("Hello Geek")

# we can use else in while loop
count = 0
while (count < 3):   
    count = count + 1
    print("Hello Geek")
else:
    print("In Else Block")



# Lists, tuples, dictionaries, and sets are all iterable objects. 
# They are iterable containers which you can get an iterator from.
# All these objects have a iter() method which is used to get an iterator

mytuple = ["apple", "banana", "cherry"]
myit = iter(mytuple)
print(next(myit))


# You can interate strings too.
mystr = "banana"
myit = iter(mystr)
print(next(myit))



# ITERABLE in python

fruits = ["apple", "orange", "kiwi"]
 
# Creating an iterator object
# from that iterable i.e fruits
iter_obj = iter(fruits)
 
# Infinite while loop
while True:
  try:
      # getting the next item
      fruit = next(iter_obj)
      print(fruit)
  except StopIteration:
      # if StopIteration is raised,
      # break from loop
       break



# SOME PRACTISE PROBLEMS
# PRINTING STARS IN PYTHON
'''
steps: 
1. We always print row by Row
2. Always start printing from left side of string
3. Blank part is printed using spaces

You should know size of pattern you wish to print: number of rows
'''


n = 5
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()


n = 5
for i in range(n):
    for j in range(i + 1):
        print('*',end=' ')
    print()


n = 5
for i in range(n):
    for j in range(i, n):
        print('*',end=' ')
    print()



n = 5
for i in range(n):
    for j in range(i, n):
        print('',end=' ')

    for j in range(i+1):
        print('*',end='')
    print()


n = 5
for i in range(n):
    for j in range(i+1):
        print(' ', end='')
    for j in range(i,n):
        print('*',end='')
    print()


