import re

txt = input()
x = re.findall(r'a+bb|bbb', txt)
print(x)