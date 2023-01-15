# program to make a simple short calculator
a= int(input("Enter the First Number:"))
b= int(input("Enter the Second Number:"))
c = input("Please Enter any one operands('+'-'*'/'**'):")
if c == "+":
    result = a+b
elif c == "-":
    if a>b:
        result = a-b
    else:
        result = b-a
elif c == "*":
    result = a*b
elif c == "/":
    if b==0:
        print("Enter an y other vaur:")
    else:
        print(a/b)
elif c == "**":
    result = a**b
else:
    print("Print only given operators next time")
print(result,"is your answer")