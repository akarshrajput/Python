a=int(input("a: "))
b=int(input("b: "))
i=1
while i<=b:
    if a%i==0 and b%i==0:
        gcd=i
    i+=1
print(gcd)