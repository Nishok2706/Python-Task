###Display n terms of natural number and their sum
number=int(input("Enter your natural number: "))
sum = 0
for i in range(1,1+number):
    print(i)
    sum+=i
print(sum)
