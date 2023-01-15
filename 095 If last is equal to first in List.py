list1=input("Enter the list: ")
data1=list1.split(",")
if data1[0]==data1[-1]:
    print("EQUAL")
else:
    print("NOT EQUAL")