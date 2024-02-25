import re

s = input()
c = re.split('_', s)
result = ''
for i in c:
    result += i.capitalize()

print(result)
