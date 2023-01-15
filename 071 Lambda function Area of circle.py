#program to calculate the area of circle using lambda function
area=lambda r: r**2*22/7
a=int(input("Enter the radius:"))
print("{:.2f}".format(area(a))," metersquares")