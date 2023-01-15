import re
myst="Hello! Good Morning, Welcome to python tutorial class 24"
x=re.findall("[e-o]+",myst)
for m in x:
    print(m)