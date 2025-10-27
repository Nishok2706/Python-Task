###Write a python program to create a calculator class.Include methods for basic arithmetic operations
#class calculator:
#    add(a,b)
#    sub(a,b)
#    mul(a,b)
#    div(a,b)

class calculator:
    def addition(self,a,b):
        return a+b
    def subtraction(self,a,b):
        return a-b
    def multiplication(self,a,b):
        return a*b
    def division(self,a,b):
        return a/b
obj_cal = calculator()
print(obj_cal.addition(8,5))
print(obj_cal.subtraction(8,5))
print(obj_cal.multiplication(8,5))
print(obj_cal.division(8,2))
