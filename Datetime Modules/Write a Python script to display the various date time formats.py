###Write a Python script to display the various date time formats
#current date and time
import datetime as d
x =d.datetime.now()
print("The current date time is",x)
#current year
print("The current year",x.year)
#Month of year
print("The current month is",x.month)
#Week number of the year
print("The current week number of the year is",x.strftime("%U"))
#Weekday of the week
print("The weekday of the week is",x.strftime("%w"))
#Day of year
print("The day of year is",x.strftime("%j"))
##Day of the month
y =x.timetuple()
print("The day of the month is",y[2])
###Day of week
print("The day of the week is",y[6])


