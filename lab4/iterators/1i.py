def n():
    N = int(input()) #мы инпутим какое то число
    for i in range(N): 
        yield i ** 2 #мы возвращаем квадрат каждого элемента 

# Using the generator
sq = n() #

# Fetch values one at a time
for square in sq:
    print(square)
