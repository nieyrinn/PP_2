import math

def calculate_polygon_area(num_sides, side_length):
    area = (num_sides * side_length**2) / (4 * math.tan(math.pi / num_sides))
    return area

# Take input for the number of sides and the length of a side from the user
num_sides = int(input())
side_length = float(input())

# Calculate the area of the regular polygon
polygon_area = calculate_polygon_area(num_sides, side_length)

# Print the result
print(polygon_area)
