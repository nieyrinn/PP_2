import re

txt = input()
x = re.findall(r'a+b*', txt)
print(x)