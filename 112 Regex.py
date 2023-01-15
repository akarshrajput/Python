import re
txt="Akarsh"
x=re.findall("^A",txt)
if x:
    print("Y")
    print(str(x))
else:
    print("N")