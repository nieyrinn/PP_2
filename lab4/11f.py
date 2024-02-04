#task 11
def is_palindrome(numbers):
    return numbers == numbers[::-1]

f = input()

if is_palindrome(f):
    print("this is palindrome!")
else:
    print("not palindrome")

