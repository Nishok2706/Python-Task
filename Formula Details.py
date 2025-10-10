###Write program calculate the below formula
Area=int(input("Enter your area: "))
Length=int(input("Enter your length: "))
Breadth=int(input("Enter your breadth: "))
Height=int(input("Enter your height: "))
Base1 =int(input("Enter your base1: "))
Base2= int(input("Enter your base2: "))
Radius = int(input("Enter your radius: "))

import math
math.pi 
Square=Area*Area
Rectangle=Length*Breadth
Triangle=1/2*Height*Breadth
Trapezoid=((Base1+Base2)*Height)/2
Cone = 1/3*math.pi*Radius**2*Height
Sphere = 4/3*math.pi*Radius**3
Cylinder = math.pi*Radius**2*Height
print("The sqaure value is",Square)
print("The rectangle value is",Rectangle)
print("The triangle value is",Triangle)
print("The trapezoid value is",Trapezoid)
print("The cone value is",Cone)
print("The sphere value is",Sphere)
print("The Cylinder value is",Cylinder)
