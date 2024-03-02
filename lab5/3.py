import re

txt = input()
x = re.findall(r'[a-n]_[a-n]', txt)
print(x)