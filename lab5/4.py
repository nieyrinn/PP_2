import re

def str(s):
    txt = re.compile(r'[A-Z][a-z]+')
    x = txt.findall(s)
    print(x)

p = input()
str(p)
