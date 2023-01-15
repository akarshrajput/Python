# program to find the sum of small consecutive numbers by using for loop
number=int(input("Enter the number:"))
sum =0
for i in range(number,0,-1):
    sum=sum+i
print(sum)