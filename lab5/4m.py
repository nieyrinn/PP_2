def f(base, h):
    area = base * h
    return area

# Take input for the length of the base and the h from the user
base = float(input())
h = float(input())

# Calculate the area of the parallelogram
p = f(base, h)

# Print the result
print(p)
