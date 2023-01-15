class Tables:  # class Table
    pass   
n=Tables()
n.name=int(input("Enter the Number: "))  # Taking the input from user.
for j in range(2,n.name+1):  # using for loop iteration.
    for i in range(1,11): 
        print(j,"x",i,"=",j*i)          
    print()