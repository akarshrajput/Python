#program to check if number is positive, negative or zero without using elif.
a=float(input("Enter the Number:"))
if a>= 0:
    if a==0:
        print("Number is Zero")
    else:
        print("Number is Positive")
else:
    print("Number is Negative")            

# second method
a=float(input("Enter the Number:"))
if a>0 :
    print(a,"is positive Number")
if a<0 :
    print(a,"is negative Number")
if a == 0:
    print(a,"is equal to Zero")       