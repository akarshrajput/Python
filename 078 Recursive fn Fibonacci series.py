#program to write a fibonacci series of given number using recursive function.
def fibonacci(num):
    if num==1: return 0
    if num==2: return 1
    return fibonacci(num-1)+fibonacci(num-2)
num=int(input("Enter the number: "))
print(fibonacci(num))