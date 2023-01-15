#program to print the factorial of any number.
number=int(input("Enter the Number: "))
i=number
factorial=1
while i>=1:
    factorial=factorial*i
    i=i-1
print("Factorial of ",number," is ",factorial)