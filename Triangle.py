###Write a program to check whether a triangle is Equilateral,isosceles,or scalene.
side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))
if side1 == side2 == side3:
        print("The triangle is Equilateral.")
elif side1 == side2 or side2 == side3 or side1 == side3:
        print("The triangle is Isosceles.")
else:
        print("The triangle is Scalene.")

