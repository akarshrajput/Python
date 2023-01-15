#program to write a factorial of given number 
def factorial(num):
    if num<=1: return 1
    return  num*factorial(num-1)
num=int(input("Enter the number: "))
print(factorial(num))