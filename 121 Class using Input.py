Emp1=input("Enter the name of Employee 1 :")
Emp2=input("Enter the name of Employee 2 :")
E=int(input("Enter the salary of this division :"))
class Finance:
    def __init__(self,name,salary):
        self.name=name
        self.gender=salary
Emp1=Finance(Emp1,E)
Emp2=Finance(Emp2,E)
print(Emp1.name,"and",Emp2.name)
print("The salary of this division is :",E)