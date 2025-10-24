###Write a python program to subtract five days from the current date
#current date = 2015-06-22
from datetime import datetime, timedelta
x = datetime(2015,6,22)
y = x -timedelta(days=5)
print("Current date is",x)
print("Date after subtracting 5 days is",y)








