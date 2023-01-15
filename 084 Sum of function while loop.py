# program to print the sum of function using while loop,.
def sumof(x):
    x=1
    sum=0
    while x<10:
        a=x*x
        sum+=a
        x=x+1
    return sum
print(sumof(10))