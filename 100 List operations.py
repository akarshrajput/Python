a=input("data: ")
b=a.split(",")
for i in range(len(b)):
    b[i]=int(b[i])
print("length:",len(b))
print("list enumerate:",list(enumerate(b)))
print("max:",max(b))
print("min:",min(b))
print("list:",b)