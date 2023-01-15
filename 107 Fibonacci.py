def fibonacci(num):
    if num==1: return 0
    if num==2: return 1
    return fibonacci(num-1)+fibonacci(num-2)
num=int(input("Enter number: "))
print(fibonacci(num))