class Person:
    def setname(self,name):
        self.name=name
    def getname(self):
        print(self.name)
class Student(Person):
    def setunivname(self,univname):
        self.univname=univname
    def getunivname(self):
        print(self.univname)
name=input("Enter name: ")
univname=input("Enter University name: ")
s1=Student()
s1.setname(name)
s1.setunivname(univname)
s1.getname()
s1.getunivname()