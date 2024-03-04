tuple1 = input()

mytuple = tuple(x.lower() == 'true' for x in tuple1.split())

result = all(mytuple)

if result:
    print("Yes")
else:
    print("No")

