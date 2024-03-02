def f(n):
    for i in range(n + 1): #размер н + 1 чтобы в конце не происходило 
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())

# Generate numbers divisible by 3 and 4
result_generator = f(n)

# Iterate and print the numbers
for number in result_generator:
    print(number)
