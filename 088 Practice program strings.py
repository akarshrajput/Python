str1=input("str: ")
if str1.startswith("Python") and str1.endswith("programming"):
    print("valid")
else:
    print("Invalid")
print("Character with min val: ",min(str1))
print("Character with max val: ",max(str1))