"""Write a python class named as personal with information function with argument of name,mail,mobile,address
Write a another class named as educational with information function with argument of marks of each subject,total,and percentage inherit education with personal
Write a another class named as bank with information function with argument of acc_number,branch_name,bank_name,ifsc_code,available_balance inherit bank with educational and
educational with personal"""


class personal:
    def __init__(self,name,mail,mobile,address):
        self.name = name
        self.mail = mail
        self.mobile = mobile
        self.address = address
    def details(self):
        print("My name is",self.name,",my mail id is",self.mail,",my mobile number is",self.mobile,"and my address is",self.address)
class educational(personal):
    def __init__(self,name,mail,mobile,address,marks,total,percentage):
        super().__init__(name,mail,mobile,address)
        self.marks=marks
        self.total=total
        self.percentage=percentage
    def information(self):
        super().details()
        print("My each subject marks are",self.marks,",my total mark is",self.total,"and my percentage is",self.percentage)
class bank(educational):
    def __init__(self,name,mail,mobile,address,marks,total,percentage,acc_number,branch_name,bank_name,ifsc_code,available_balance):
        super().__init__(name,mail,mobile,address,marks,total,percentage)
        self.account=acc_number
        self.branch=branch_name
        self.bank=bank_name
        self.ifsc=ifsc_code
        self.available=available_balance
    def overall(self):
        super().information()
        print("My account number is",self.account,",my branch name is",self.branch,",my bank name is",self.bank,",my ifsc code is",self.ifsc,"and my available is",self.available)
obj_total = bank("Nishok","nishoklibin@gmail.com",9952605893,"Madurai",[69,77,81,97,92],416,86.2,628748858286,"Bypass","SBI",789654321,22150)
obj_total.overall()
        
        
