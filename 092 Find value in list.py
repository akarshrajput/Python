data=input("Enter List: ")
list1=data.split(",")
value=input("Enter value: ")
if value in data:
    print(value,"is present in data")
else:
    print(value,"is not present in data")
print("First element: ",list1[0],"Last element: ",list1[-1])