import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return distance

# Пример использования
point1 = Point(1, 2)
point2 = Point(4, 6)

print("Initial coordinates:")
point1.show()
point2.show()

new_x, new_y = 3, 5
point1.move(new_x, new_y)

print(f"\nAfter moving to ({new_x}, {new_y}):")
point1.show()

distance = point1.dist(point2)
print(f"\nDistance between the points: {distance}")
