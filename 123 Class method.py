# classmethod is used to change the salary increment
class Finance:
    increment=1.5
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def increase(self):
        self.salary=int(Finance.increment*self.salary)     
    @classmethod
    def change_increment(cls,amount):
        cls.increment=amount
akarsh=Finance("Akarsh",44000)
sujal=Finance("Sujal",44000)
print(akarsh.name)
Finance.change_increment(2)
akarsh.increase()
print(akarsh.salary)
print(sujal.name)
Finance.change_increment(1.5)
sujal.increase()
print(sujal.salary)