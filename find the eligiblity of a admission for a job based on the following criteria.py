###Program to find the eligiblity of a admission for a job based on the following criteria
Aptitude=int(input("Enter the Aptitue mark: "))
GD = int(input("Enter the GD mark: "))
Technical = int(input("Enter the Technical mark: "))
HR=int(input("Enter the HR mark: "))
Total_Marks = Aptitude+GD+Technical+HR
print("Total Marks",Total_Marks)
if Aptitude>=85 and GD>=90 and Technical>=80 and HR>=95:
    if Total_Marks>=390 and Total_Marks<=400:
        print("Your are eligible and your salary is 30000")
    elif Total_Marks>=380 and Total_Marks<390:
        print("Your are eligible and your salary is 28000")
    elif Total_Marks>=370 and Total_Marks<380:
        print("Your are eligible and your salary is 25000")
    elif Total_Marks>=350 and Total_Marks<370:
        print("Your are eligible and your salary is 20000")
else:
    print("Not Eligible")
