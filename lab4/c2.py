#task 2
class Shape:
    def area(self):
        print("Area of the shape: 0")


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        area_value = self.length ** 2
        print(area_value)


# Пример использования
shape_instance = Shape()
shape_instance.area()

user_length = float(input())
square_instance = Square(user_length)
square_instance.area()
