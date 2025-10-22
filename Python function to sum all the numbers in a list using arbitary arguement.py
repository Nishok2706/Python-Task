###Python function to sum all the numbers in a list using arbitary arguement

def sum(*a):
    sum = 0
    for i in a:
        sum+=i
    print("The sum of total number is",sum)
sum(2,3,4,5,6)
sum(85,45,50,50,55,15)
