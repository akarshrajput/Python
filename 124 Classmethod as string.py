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
    @classmethod
    def from_str(cls,emp_string):
        name,salary=emp_string.split("-")
        return cls(name,salary)

akarsh=Finance("Akarsh",44000)
sujal=Finance("Sujal",44000)
raj=Finance.from_str("Raj-42000")
print(akarsh.name)
Finance.change_increment(2)
akarsh.increase()
print(akarsh.salary)
print(raj.name)