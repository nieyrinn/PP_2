import math

def area(side, lenght):
    area = (side * lenght**2) / (4 * math.tan(math.pi / side))
    return area

side = float(input())
lenght = float(input())

result = area(side, lenght)

print(result)
