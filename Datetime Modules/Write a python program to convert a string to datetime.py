###Write a python program to convert a string to datetime

from datetime import datetime
x = "27-06-1998"
y = datetime.strptime(x, "%d-%m-%Y")
print(y)



from datetime import datetime
x = "1998-06-27"
y = datetime.strptime(x, "%Y-%m-%d")
print(y)




from datetime import datetime
x = "June 27,1998"
y = datetime.strptime(x,"%B %d,%Y")
print(y)




