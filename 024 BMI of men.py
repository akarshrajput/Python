# program to calculate the BMI of men in India.
x=input("Enter the name of men:")
a=float(input("Enter the mass of men (in Kg):"))
b=float(input("Enter the height of men (in meteres)"))
c=a/(b**2)
print("BMI is:",c)
print("Normal range of BMI is 18.5-24.9")
if c>=18.5 and c<= 24.9:
    print(x," is Normal")
elif c>24.9 and c<=29.9:
    print(x," is Overweight")
elif c>29.9:
    print(x," is Obese")
elif c<18.5:
    print(x," is Underweight")        