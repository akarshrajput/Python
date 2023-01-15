print("Welcome to Darkweb")
from getpass import getpass
a=int(getpass(prompt="Password 1: ")) 
b=int(getpass(prompt="Password 2: "))     
if a==int(0b10011010010) and b==int(0b10011000111010):
    print("You are welcome in our dark world!")
    g=input("First name: ")
    h=input("Last Name: ")
    j=input("Enter your Mobile Number: ")
    i=input("Welcome "+g+" "+h+" what do you want: ")
    k=input("Please enter last four digit of your mobile number for confirmation: ")
    if k==j[6:]:
        print("Mobile Number confirmed successfully!")
        print("OK!",g," You will get",i," soon!")
        print("We will contact you later for",i,"on your Mobile Number:",j,"for address related services.")
        print("Thank you for our services, Mr."+g+" "+h)
    else:
        print("Failed to proceed")
else:
    print("Access denied")