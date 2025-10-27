###write a python program to create a class that represents a shape.
#Include methods to calculate its area and perimeter
#Implement subclasses for shapes like circle,triangle and square.
#class circle
### area(r),A=3.14*r*r
### perimeter(r),C = 2*3.14*r
#class triangle
###area(l,b),A = 1/2*b*h
##Perimeter(a,b,c),P = a+b+c
###Class square
#area(a) A = A*A
#Perimeter(a),P=4a
class Shape:
    pass
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r
    def perimeter(self):
        return 2 * 3.14 * self.r
class Triangle(Shape):
    def __init__(self, b, h, a1, a2, a3):
        self.b = b
        self.h = h
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
    def area(self):
        return 0.5 * self.b * self.h
    def perimeter(self):
        return self.a1 + self.a2 + self.a3
class Square(Shape):
    def __init__(self, a):
        self.a = a
    def area(self):
        return self.a * self.a
    def perimeter(self):
        return 4 * self.a
c = Circle(8)
t = Triangle(6, 4, 3, 4, 5)
s = Square(8)
print("Circle area:", c.area())
print("Circle perimeter:", c.perimeter())
print("Triangle area:", t.area())
print("Triangle perimeter:", t.perimeter())
print("Square area:", s.area())
print("Square perimeter:", s.perimeter())

