text = input().split()

with open('5.py', 'w') as myfile:
    for c in text:
        myfile.write("%s\n" % c)

content = open('text.py')
print(content.read())