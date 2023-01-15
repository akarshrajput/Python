#program to find the ticket of travelling
a=int(input("Enter the distance of travelling:"))
if a>1 and a<=50:
    print("You should pay Rs",a*2)
if a>50 and a<=100:
    print("You should pay Rs",a*4)
if a>100:
    print("You should pay Rs",a*5)
