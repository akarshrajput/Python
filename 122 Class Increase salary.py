class Finance:
    increment=1.5
    number_of_Employee=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Finance.number_of_Employee +=1

    def increase(self):
        self.salary=int(Finance.increment*self.salary)
        
akarsh=Finance("Akarsh",44000)
sujal=Finance("Sujal",44000)
akarsh.increase()
print(akarsh.name,sujal.name)
print(akarsh.salary)
print("Number of Employees :",Finance.number_of_Employee)
print(akarsh.__dict__)
print(Finance.__dict__)