#task 3
def f(heads, legs):
    rabbits = (legs - 2 * heads) / 2 #2 × chickens + 4 × rabbits = legs
    chickens = heads - rabbits #chickens = heads − rabbits
    return int(chickens), int(rabbits)
heads = int(input())
legs = int(input())
result = f(heads, legs)
print(result[0], result[1])