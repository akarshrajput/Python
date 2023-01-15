a=int(input("Enter the year: "))
if a%400==0:
    print(a,"is Leap year")
elif a%4==0 and a%100!=0:
    print(a,"is Leap year")
else:
    print("Not a Leap Year")