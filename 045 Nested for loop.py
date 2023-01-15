a=int(input("Enter the number of line:"))
for i in range(a):
    for j in range(i+1):
        print(j+1,end=" ")
        j=j+1
    print()