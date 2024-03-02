def even_numbers_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

# Input
n = int(input())

even_numbers = even_numbers_generator(n)

# Print even numbers in comma-separated form
print(','.join(map(str, even_numbers)))
