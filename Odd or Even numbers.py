###Count the number of even and odd numbers from a series of numbers.
number = int(input("Enter the number: "))
odd_number=0
even_number=0
for i in range(1,number+1):
    if i%2==0:
        even_number+=1
    else:
        odd_number+=1
print("The count of even number is",even_number)
print("The count of odd number is",odd_number)
