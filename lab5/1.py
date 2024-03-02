import re

def str():
    s = input()
    txt = re.compile(r'a+b*')
    x = txt.fullmatch(s)
    if x:
        print("yes")
    else:
        print("no")

str()
