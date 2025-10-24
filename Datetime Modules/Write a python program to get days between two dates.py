###Write a python program to get days between two dates
#sample date : 2000,2,28,2001,2,28
#Excepted output: 366 days, 0:00:00


import datetime
x = datetime.datetime(2000,2,28)
y = datetime.datetime(2001,2,28)
z = y - x
print("The difference between two dates is",z)
