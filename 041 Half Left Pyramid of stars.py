#program to make a half pyramid of stars
a=int(input("Enter the number of line:"))
for i in range(a):
    for j in range(i+1):
        print("*",end=" ")
    print()