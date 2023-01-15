#program to find cube elements of list with using map function
def addone(num):
    return num**3
list1=[1,2,3,4]
print(list(map(addone,list1)))