def retnum(num):
    return num
def double(num):
    return num*2
def thrice(num):
    return num*3
def fourtime(num):
    return num*4
def printfunction(*num):
    for i in num:
        print('final function:',i)
printfunction(retnum(2),double(2),thrice(2),fourtime(2))