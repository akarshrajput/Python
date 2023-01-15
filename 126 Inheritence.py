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

class Programmer(Finance):
    def __init__(self, name, salary, proglang, exp):
        super().__init__(name, salary)
        self.prolang=proglang
        self.exp=exp
lovepreet=Programmer("Lovepreet",22000,"Python","5 yrs")
print(akarsh.name)
print(lovepreet.exp)