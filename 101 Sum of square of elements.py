data=input("data: ")
list1=data.split(",")
for i in range(len(list1)):
    list1[i]=int(list1[i])
print("sum:",sum(list1))
for i in range(len(list1)):
    d=i*2
    print("squares:",d)
print("sum of squares:",sum(d))