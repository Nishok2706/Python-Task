"""Write a python class named as school with information function(name,mail,mobile,adddress)
Write a another class named as staff with staff information with argument of name,mail,mobile,address,dept
Write a another class named as student with student information with argument of name,mail,mobile,address,dept
inherit student with school and staff with school
Ask whether student or staff to user and call the function according to the user"""
class school:
    def __init__(self,name,mail,mobile,address):
        self.name = name
        self.mail = mail
        self.mobile = mobile
        self.address = address
    def school_details(self):
        print("My name is",self.name,",my mail id is",self.mail,",my mobile number is",self.mobile,"and my address is",self.address)
class staff(school):
    def __init__(self,name,mail,mobile,address,dept):
        super().__init__(name,mail,mobile,address)
        self.department=dept
    def staff_details(self):
        super().school_details()
        print("My department is",self.department)
class student(school):
    def __init__(self,name,mail,mobile,address,dept):
        super().__init__(name,mail,mobile,address)
        self.department=dept
    def student_details(self):
        super().school_details()
        print("My department is",self.department)
user = input("Enter whether your student or staff: ").strip().lower()
if user == "student":
    obj = student("Nishok", "nishok@gmail.com", 9952605893, "Madurai", "ECE")
    obj.student_details()
elif user == "staff":
    obj = staff("Libin", "Libin@gmail.com", 9876543210, "Chennai", "CSE")
    obj.staff_details()
else:
    print("Invalid input")
