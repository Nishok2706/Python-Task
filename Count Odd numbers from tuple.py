###Count odd numbers,how many odd numbers are in (1,2,3,4,5)
numbers = (1,2,3,4,5)
count = 0
for i in numbers:
    if i%2!=0:
        count+=1
print("The odd numbers count are:",count)
