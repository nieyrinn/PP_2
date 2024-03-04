import math

n = input()

mylist = [int(x) for x in n.split()]

result = math.prod(mylist)

print(result)
