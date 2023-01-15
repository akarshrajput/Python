#program to find the sum of factorial
n=int(input("Enter the Number:"))
i=n
sum=0
while i>=1:
    sum=sum+i
    i=i-1
print("Sum of ",n," is ",sum)