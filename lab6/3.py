import re
 
def str(s):
    txt = re.compile(r'\w+_\w+')
    x = txt.findall(s)
    print(x)

p = input()
str(p)

