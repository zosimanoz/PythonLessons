"""
Files are named locations on disk to store related information. 
They are used to permanently store data in a non-volatile memory (e.g. hard disk).

When we want to read from or write to a file, we need to open it first. 
When we are done, it needs to be closed so that the resources that are tied with the file are freed.


Basic Operations: OPEN FILE -> READ/WRITE FILE -> CLOSE FILE

"""


"""
Opening Files in Python: 

Python has a built-in open() function to open a file. 
This function returns a file object, also called a handle, as it is used to read or modify the file accordingly.

"""

f = open("test.txt")    # open file in current directory
f = open("C:/Python38/README.txt")  # specifying full path


"""

We can specify the mode while opening a file. In mode, we specify whether we want to read r, write w or append a to the file. 
We can also specify if we want to open the file in text mode or binary mode.

The default is reading in text mode. In this mode, we get strings when reading from the file.

On the other hand, binary mode returns bytes and this is the mode to be used when dealing with non-text files like images or executable files.

"""

f = open("test.txt")      # equivalent to 'r' or 'rt'
f = open("test.txt",'w')  # write in text mode
f = open("img.bmp",'r+b') # read and write in binary mode

# It is better to specify encoding type while opening file, since encoding is platform dependent
f = open("test.txt", mode='r', encoding='utf-8')


"""

CLOSING A FILE: 
Closing a file will free up the resources that were tied with the file. It is done using the close() method available in Python.

"""

f = open("test.txt", encoding = 'utf-8')
# perform some file operations
f.close()

"""
This method is not entirely safe. If an exception occurs when we are performing some operation with the file, the code exits without closing the file.

A safer way is to use a try...finally block.
"""

try:
   f = open("test.txt", encoding = 'utf-8')
   # perform file operations
finally:
   f.close()


"""
The best way to close a file is by using the with statement. 
This ensures that the file is closed when the block inside the with statement is exited.
It closes file internally. We need not manually close it.
"""

with open("test.txt", encoding = 'utf-8') as f:
    #perform file operations


"""
In order to write into a file in Python, we need to open it in write w, append a or exclusive creation x mode.
"""

with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")


"""
This program will create a new file named test.txt in the current directory if it does not exist. 
If it does exist, it is overwritten.
"""

"""
READING FILES: 
To read a file in Python, we must open the file in reading r mode.

There are various methods available for this purpose. We can use the read(size) method to read in the size number of data. 
If the size parameter is not specified, it reads and returns up to the end of the file.
"""

f = open("test.txt",'r',encoding = 'utf-8')
f.read(4) # read the first 4 data
f.read(4) # read the next 4 data
f.read()  # read in the rest till end of file
f.read()  # further reading returns empty sting

"""
We can change our current file cursor (position) using the seek() method. 
Similarly, the tell() method returns our current position (in number of bytes).
"""

f.tell()    # get the current file position
f.seek(0)   # bring file cursor to initial position
print(f.read())  # read the entire file