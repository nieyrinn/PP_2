class Shape:
    def area(self):
        print("Area of the shape: 0")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area_value = self.length * self.width
        print(area_value)

user_length = float(input())
user_width = float(input())

rectangle_instance = Rectangle(user_length, user_width)
rectangle_instance.area()
