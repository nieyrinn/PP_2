import re
 
def str(s):
    txt = re.compile(r'a.*b')
    x = txt.findall(s)
    print(x)

p = input()
str(p)

