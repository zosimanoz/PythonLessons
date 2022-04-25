"""
creating strings
"""

my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)


"""
How to access characters in a string?
"""

#Accessing string characters in Python
str = 'programiz'
print('str = ', str)

#first character
print('str[0] = ', str[0])

#last character
print('str[-1] = ', str[-1])

#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])

#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])


"""
Changing a string: Strings are immutable
"""

my_string = 'programiz'
my_string[5] = 'a'

"""
We cannot delete or remove characters from a string. But deleting the string entirely is possible using the del keyword.
"""

del my_string[1]
del my_string


"""
Few string functions:
"""

"PrOgRaMiZ".lower()
"PrOgRaMiZ".upper()
"This will split all words into a list".split()
' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string'])
'Happy New Year'.find('ew')
'Happy New Year'.replace('Happy','Brilliant')
