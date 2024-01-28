#Ex 1
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Ex 2
#The bool() function allows you to evaluate any value, and give you True or False in return,
print(bool("Hello"))
print(bool(15))\

#Ex 3 
#the following will return false:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#Ex 4
#One more value, or object in this case, evaluates to False, 
#and that is if you have an object that is made from a class with a __len__ function that returns 0 or False
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#Ex 5
#Functions can Return a Boolean
#You can create functions that returns a Boolean Value:
def myFunction() :
  return True

print(myFunction())

#Ex 6
#Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
