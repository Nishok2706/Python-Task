###Write a python class named as personal with information function with argument of the name,mail,mobile,address
###Write a another class named as educational with information function with argument of marks of each subject,total,and percentage inherit education with personal

class person:
    def __init__(self,name,mail,mobile,address):
        self.name = name
        self.mail = mail
        self.mobile = mobile
        self.address = address
    def details(self):
        print("My name is",self.name,", my mail id is",self.mail,"my mobile number is",self.mobile,"and my address is",self.address)
class education(person):
    def __init__(self,name,mail,mobile,address,marks,total,percentage):
        super().__init__(name,mail,mobile,address)
        self.marks=marks
        self.total=total
        self.percentage=percentage
    def information(self):
        super().details()
        print("My marks are",self.marks,",my total is",self.total,"and my percentage is",self.percentage)
obj_details = education("Nishok","nishoklibin@gmail.com",9952605893,"Madurai",[69,77,81,97,92],416,83.2)
obj_details.information()




