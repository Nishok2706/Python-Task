###Find Smallest Number - Find the smallest value in (45, 12, 89, 33, 67) using a loop.

numbers = (45,12,89,33,67)
smallest = numbers[0]
for i in numbers:
    if i < smallest:
        smallest = i
print("The smallest value is",smallest)
    
