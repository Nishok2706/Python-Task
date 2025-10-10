###A company decides to give a bonus of 5% to employee if his/her year of service is more than 5 years.
###Ask user for their salary and year of service and print the net bonus amount
Year_of_service = int(input("Enter your year of service: "))
salary = int(input("Enter the salary: "))
if Year_of_service >5:
    Total_Bonus_Amount=salary*0.05
    print("Your net bonus amount is",Total_Bonus_Amount)
else:
    print("Your year of service is not eligible for the bonus amount")
