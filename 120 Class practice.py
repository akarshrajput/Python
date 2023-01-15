class About:
    def __init__(self,name,rollno,gender,marks):
        self.name=name
        self.rollno=rollno
        self.gender=gender
        self.marks=marks
akarsh=About("Akarsh",1,"Male",98)
sujal=About("Sujal",2,"Male",90)
print(akarsh.name,"and",sujal.name)