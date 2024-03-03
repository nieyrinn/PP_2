def square():
    n = int(input()) 
    for i in range(n + 1): 
        yield i ** 2 

for x in square():
    print(x)

