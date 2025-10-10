###Get two values from user and type
#a. + for addition
#b. - for subtraction
#c. * for multiplication
#d. / for division

first_value=int(input("Enter the first number: "))
second_value=int(input("Enter the second number: "))
which_type= input("Addition/Subtraction/Multiplication/Division: ")
if which_type =="Addition":
    print("The sum of two numbers is",first_value+second_value)
elif which_type =="Subtraction":
    print("The difference of two numbers is",first_value-second_value)
elif which_type =="Multiplication":
    print("The product of two numbers is",first_value*second_value)
elif which_type =="Division":
    print("The number after division is",first_value/second_value)
else:
    print("Enter the correct type")
