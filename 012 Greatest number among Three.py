# program to find the larger number among three number.
a=float(input("Enter the number 1:"))          
b=float(input("Enter the number 2:")) 
c=float(input("Enter the number 3:"))
if a>b:
    if a>c:
        print(a,"is Greater Number")  
    else:
        print(c,"is Greater Number")
else:
    if b>c:
        print(b,"is Greater Number")
    else:
        print(c,"is Greater Number")    

# second method
a=float(input("Enter the number 1:"))          
b=float(input("Enter the number 2:")) 
c=float(input("Enter the number 3:"))
if a>= b and a>=c:
    print(a,"is Greater")
if b>a and b>c:
    print(b,"b is Greater")
if c>a and c>b:
    print(c,"is Greater")        

