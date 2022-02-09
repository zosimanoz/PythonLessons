x,y =2,8
if(x < y):
    st= "x is less than y"
    print(st)


# What happen when “if condition” does not meet ?

x,y =8,4
if(x < y):
	st= "x is less than y"
else:
	st= "x is greater than y"
print (st)


# When “else condition” does not work ?

x,y =8,8
if(x < y):
	st= "x is less than y"
else:
	st= "x is greater than y"
print(st)

# here else gives wrong output, we need elif

x,y =8,8
if(x < y):
	st= "x is less than y"
elif (x == y):
	st= "x is same as y"
else:
	st="x is greater than y"
print(st)


# How to execute conditional statement with minimal code ?
x,y = 10,8
st = "x is less than y" if (x < y) else "x is greater than or equal to y"
print(st)


# NESTED IF-ELSE

total = 100
#country = "US"
country = "AU"
if country == "US":
    if total <= 50:
        print("Shipping Cost is  $50")
elif total <= 100:
    print("Shipping Cost is $25")
elif total <= 150:
	print("Shipping Costs $5")
else:
    print("FREE")
if country == "AU": 
	if total <= 50:
	    print("Shipping Cost is  $100")
else:
	print("FREE")



# switch case python

def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
 
    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return switcher.get(argument, "nothing")

print(numbers_to_strings(0))


val = '5'
match val:
  case '1':
    print("One")
  case '2':
    print("Two")
  case _:
    print("default")