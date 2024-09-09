# we can use datetime module to work with dates

import datetime as dt

# making a current date and time object
currentdate = dt.datetime.now() # print 2024-07-07 16:07:51.166382
print(currentdate)

# extracting variables
print(currentdate.day)
print(currentdate.month)
print(currentdate.year)
print(currentdate.hour)
print(currentdate.minute)
print(currentdate.second)

# strftime() function
print(currentdate.strftime("%A")) # print Sunday with %A - print sun with %a
print(currentdate.strftime("%B")) # print July with %B - print  Jul with %b
print(currentdate.strftime("%Y")) # print 2024 with %Y - print  24 with %y
print(currentdate.strftime("%c")) # Sun Jul  7 16:18:24 2024
print(currentdate.strftime("%C")) # print century
print(currentdate.strftime("%p")) # print AM| PM
print(currentdate.strftime("%z")) # print zone

# creating a date object
x = dt.datetime(2020,4,5)
print(x)