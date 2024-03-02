import re

def str(s):
    txt = re.compile(r'a(bb|bbb)')
    x = txt.match(s)
    if x:
        print("Yes")
    else:
        print("No")

p = input()
str(p)
