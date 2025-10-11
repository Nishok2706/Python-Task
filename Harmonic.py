###Program to display the n terms of harmonic series and their sum.
number=int(input("Enter the number: "))
sum = 0
for i in range(1,number+1):
    print("1/",i)
    sum=sum+1/i
print("The sum of a harmonic series of a given number is",sum)


