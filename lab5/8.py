import re

s = input()
x = re.findall(r'[A-Z]', s)

for i in x:
    print(i, end='')

