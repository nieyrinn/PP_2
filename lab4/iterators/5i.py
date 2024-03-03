def f():
    n = int(input())
    while n >= 0:
        yield n
        n -= 1

for x in f():
    print(x)
