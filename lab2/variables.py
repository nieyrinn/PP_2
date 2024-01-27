#Ex 0
x = 5
y = "Hello, World!"
#In Python, variables are created when you assign a value to it.

#Ex 1
x = 5
y = "John"
print(x)
print(y)
#Python has no command for declaring a variable.

#Ex 2
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
#Variables do not need to be declared with any particular type, and can even change type after they have been set.

#Ex 3
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
#If you want to specify the data type of a variable, this can be done with casting.

#Ex 4
x = 5
y = "John"
print(type(x))
print(type(y))
#You can get the data type of a variable with the type() function.

#Ex 5
x = "John"
# is the same as
x = 'John'
#String variables can be declared either by using single or double quotes

#Ex 6
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
#legal variable names

#Ex 7
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#multiple values

#Ex 8
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
#In the print() function, you output multiple variables, separated by a comma.

#Ex 9
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
#Create a variable outside of a function, and use it inside the function

#Ex 10
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#same