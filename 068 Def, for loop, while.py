def numbers1(*numbers):
    for number in numbers :
        num=0
        while(num < len(numbers)):
            if numbers[num] % 2 == 0:
                print(numbers[num], end=" ")
    num+=1
numbers1(3,4,5)