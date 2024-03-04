def is_palindrome():
    s = input()
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

if is_palindrome():
    print("yes")
else:
    print("no")
