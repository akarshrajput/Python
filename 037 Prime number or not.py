#program to check if number is prime or not prime
a=int(input("Enter the number:"))
if a==2:
    print("Yes!",a,"is a prime number")
elif a%2==0:
    print("No!",a,"is not the prime number")
elif a%1==0 and a%a==0:
    print("Yes!",a,"is a prime number")