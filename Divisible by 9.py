###Program to find the number and sum of all integer between 100 and 200 which are divisible by 9.
sum=0
for i in range(100,200):
    if (i%9==0):
      print(i)
      sum=sum+i
print("The number and sum of all integer between 100 and 200 which are divisible by 9 is",sum)
