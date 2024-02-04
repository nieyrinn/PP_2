#task 12
def histogram(numbers):
    for num in numbers:
        print('*' * num)

f = input()
numbers = [int(x) for x in f.split()]

histogram(numbers)

