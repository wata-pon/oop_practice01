'''
# 半径1の円
circle1 = Circle(radius=1)
print(circle1.area())  # 3.14
print(circle1.perimeter())  # 6.28

# 半径3の円
circle3 = Circle(radius=3)
print(circle3.area())  # 28.27
print(circle3.perimeter())  # 1 8.85

classCircle:
属性:
    -半径
    -面積 r*r*π
    -円周の長さ 2*r*π
ルール:
    -表示するときは、小数点第2位まで
'''


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (self.radius ** 2)

    def perimeter(self):
        return (self.radius * 2)


circle1 = Circle(radius=1)

print(circle1.area)
