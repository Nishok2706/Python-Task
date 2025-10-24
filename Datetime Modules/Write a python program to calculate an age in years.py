###Write a python program to calculate an age in years

from datetime import datetime

x = datetime.today()
birthday = datetime(1998,6,27)
age = x-birthday
print(age)
