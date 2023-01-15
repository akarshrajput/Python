a=int(input("Enter side 1: "))
b=int(input("Enter side 2: "))
c=int(input("Enter side 3: "))
if a==b and b==c and c==a:
    print("Triangle is Equilateral")
elif a!=b and b!=c and c!=a:
    print("Triangle is Scalene")
else:
    print("Triangle is Isosceles")