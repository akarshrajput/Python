#program to find if alphabet is vowel or not
a=str(input("Enter the alphabet :"))
b="abcdefghijklmnopqrstuvwxyz"
if a==b[4] or a==b[0] or a==b[8] or a==b[14] or a==b[20]:
    print("Number is vowel")
else:
    print("Number is not a vowel")
