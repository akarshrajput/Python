#program to take the password three times and if wrong then denied the access
passwordMatched = False
password=""
while i<=3:
    password= input("Enter password")
    if password =="abc":
        passwordMatched=True
        break
    else:
        print("Invalid Password")
    i=i+1
if passwordMatched==True:
    print("Login succesful!")
else:
    print("Access denied")