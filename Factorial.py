###Program to calculate the factorial of a given number
number = int(input("Enter the number: "))
factorial = 1
if number<0:
    print("The negative number for factorial does not exist")
elif number ==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,number+1):
        factorial*=i
    print("The factorial of ",number,"is",factorial)
