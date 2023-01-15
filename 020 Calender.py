# program to find the calendar of particular month of particular year
import calendar
a=int(input("Enter year:"))
b=int(input("Enter month:"))
year = a
month = b
print(calendar.month(year,month))