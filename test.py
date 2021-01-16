import random

if 5 > 2:
	print("Five is greater than 2")
if 6 > 2:
	print("Six is greater than 2")
#comments
"""
multiple lines
can be commented out
like this
"""
x= "Brian"
y= 10
print(x)
print(y)
y="Coding is fun!"
print(x + " says " + y)

"""
Rules for variables in Python according to W3schools:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
"""

print("x is a variable")

x, y, z ="1", "2", "3"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

x=5
y=10
z=x+y
print(z)

z="twenty-three"
print(z)

#define your own function
def myFunc():
	#assign a global variable in a local setting
	global z
	z = "twenty-one"
	a = "twenty"
	print("i used to be " + a + " years old.")

#call your function
myFunc()

print(z)
#print data type of z
print(type(z))

#print random number from 1-10
print(random.randrange(1,11))

multilineString = """
this is a string that can stretch
across several lines of code by using
the triple quotes
"""

#print multilineString
print(multilineString)

s = "Hello, world!"
#print the character at position 1 (positions start at 0)
print(s[1])
#get a range of characters from position 2 until position 5 (not included)
print(s[2:5])
#negative indexing, count from the end of the string
print(s[-5:-2])
#print the length of a string
print(len(s))
#strip() method removes any white space from the beginning or the end of a string
a= "   Hello, World!   "
print(a.strip())
#lower() returns the string in all lower case
print(a.lower())
#upper() returns the string in all upper case
print(a.upper())
#replace() replaces a string with another string
print(a.replace("H", "J"))
#split() splits the string into substrings if it finds an instance of the separator
print(a.split(","))
#check for a substring in a string
check = "ell" in a
print(check)
#check for a substring in a string
check = "ell" not in a
print(check)

# a way to print int in a string using {} and the format() method
age = 31
words = "my age is {}"
print(words.format(age))

#format multiple variables into a string
quantity = 5
itemNumber = 496
price = 24.99
order = "I would like {} of item {} for the price of {} each."
print(order.format(quantity, itemNumber, price))
#can use index numbers to ensure they are in the correct locations
order = "I would like to pay {2} for {0} of item number {1}."
print(order.format(quantity, itemNumber, price))

#use \ to escape special characters
text = "my favorite football team's name is \"Vikings\""
print(text)
#lots of different methods built into python for strings
t="banana"
#string will take up 20 spaces and place 'banana' in the center
print(t.center(20))
#capitalize
print(t.capitalize())
#counts number of instances of whatever
print(t.count("a"))
#returns true if string ends with value
print(t.endswith("a"))
