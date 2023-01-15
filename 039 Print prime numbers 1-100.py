#program to print all prime numbers from 1 to 100
for j in range(1,101):
    isprimenumber=True
    for i in range(2,j):
        if j%i==0:
            isprimenumber=False
            break
    if isprimenumber==True:
            print(j,"is prime")
