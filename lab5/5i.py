def f(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())

# Generate and print countdown using the generator
for number in f(n):
    print(number)
