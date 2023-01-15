# program to print even numbers from any range of numbers
print("Attention: If the number you are writting is even then that number will also print in your terminal.")
print("Now carry on_")
a=int(input("From : "))
b=int(input("Till : "))
b+=1
for i in range(a,b,2):
    print(i ,end=" ")