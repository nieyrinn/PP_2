def even():
    n = int(input())
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

for x in even():
    print(x)
