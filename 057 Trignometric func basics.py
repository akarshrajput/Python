import math
r1=math.radians(0)
r2=math.radians(30)
r3=math.radians(45)
r4=math.radians(60)
r5=math.radians(90)
print("Degree  0  30  45  60  90")
print("sin", math.sin(r1),  math.sin(r2),  math.sin(r3),  math.sin(r4),  math.sin(r5))
print("cos", math.cos(r1),  math.cos(r2),  math.cos(r3),  math.cos(r4),  math.cos(r5))
print("tan", math.tan(r1),  math.tan(r2),  math.tan(r3),  math.tan(r4),  math.tan(r5))

# or second formula using list
degrees=[0,30,45,60,90]
for i in degrees:
    radian=math.radians(i)
    print("sin("+str(i)+"): ",math.sin(radian))
    print("cos("+str(i)+"): ",math.cos(radian))
    print("tan("+str(i)+"): ",math.tan(radian))