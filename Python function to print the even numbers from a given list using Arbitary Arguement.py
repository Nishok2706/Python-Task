###Python function to print the even numbers from a given list using Arbitary Arguement

def even(*a):
    even_number=0
    for i in a:
        if i%2==0:
            print("The even numbers are",i)
even(1,2,3,4,5,6,7,8,9,10,11,12,13,14)
