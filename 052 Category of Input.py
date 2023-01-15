a=input("Enter the number: ")
b="abcdefghijklmnopqrstuvwxyz"
c="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
d="1234567890"
if a[0] in b:
    print("alphabet")
elif a[0] in c:
    print("alphabet")
elif a[0] in d:
    print("digit")
else:
    print("character")