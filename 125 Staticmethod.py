# Static method used for making independent function
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
    
    @staticmethod
    def isopen(day):
        if day=="sunday":
            return False
        else:
            return True
print(Finance.isopen("sunday"))
print(Finance.isopen("monday"))
shubham=Finance("Shubham",22000)
print(Finance.isopen("sunday"))