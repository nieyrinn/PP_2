#Ex 1
print("Hello")
print('Hello')
# 'hello' is the same as "hello"

#Ex 2
a = "Hello"
print(a)
#Assigning a string to a variable is done with the variable name followed by an equal sign and the string

#Ex 3
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#You can use three double quotes

#Ex 4
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
#Or three single quotes

#Ex 5
a = "Hello, World!"
print(a[1])

#Ex 6
b = "Hello, World!"
print(b[2:5])
#Get the characters from position 2 to position 5 (not included)

#Ex 7
a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())
# upper and lower methods

#Ex 8
a = "Hello"
b = "World"
c = a + b
print(c)
#Merge variable a with variable b into variable c

a = "Hello"
b = "World"
c = a + " " + b
print(c)
#to add a space between them, add a " "

#Ex 9
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#Use the format() method to insert numbers into strings

#Ex 10
txt = "We are the so-called \"Vikings\" from the north."
#The escape character allows you to use double quotes when you normally would not be allowed:
