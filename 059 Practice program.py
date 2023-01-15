a=int(input())
b=int(input())
if a==6 or b==6:
    print("True")
elif a+b==6:
    print("True")
elif a-b==6 or b-a==6:
    print("True")
else:
    print("False")