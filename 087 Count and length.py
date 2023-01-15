a=input("Enter URL: ")
print(a.count("."))
for i in range(len(a)):
    if a[i]==".":
        print(i,end=" ")
