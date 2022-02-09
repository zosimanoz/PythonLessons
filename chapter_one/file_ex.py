
# f = open("test.txt", mode="w", encoding='utf-8')
# f.write("Hi thi is second line")
# f.close()

# f = open("test.txt", mode="r", encoding='utf-8')
# print(f.read())
# f.close()

# with open("test2.txt",'w',encoding = 'utf-8') as f:
#    f.write("my first file\n")
#    f.write("This file\n\n")
#    f.write("contains three lines\n")


with open("test2.txt",'r',encoding = 'utf-8') as f:
   print(f.tell())    # get the current file position
   print(f.read(4))
   print(f.tell())
   f.seek(10)
   print(f.tell())
   # f.seek(0)   # bring file cursor to initial position
   # print(f.read())  # read the entire file


