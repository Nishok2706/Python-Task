###Write a python program to print today,yesterday,tommorrow

from datetime import datetime,timedelta

x= datetime.today()
y = x-timedelta(days=1)
z = x+timedelta(days=1)
print("The current day is",x)
print("The yesterday is",y)
print("The tommorrow is",z)
