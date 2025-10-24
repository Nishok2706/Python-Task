###Write a python program to convert a string to a datetime
#Samplestring:July 1 14 2:43pm
#Excepted output: 2014-07-01 14:43:00

from datetime import datetime
x = "July 1 14 2:43pm"
y = datetime.strptime(x, "%B %d %y %I:%M%p")
print(y)
