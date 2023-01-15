#num=int(input("Enter the number: "))
#for i in range (1,int((num/2)+1)):
#    if num%i==0:
#        print(i)

def sum_div(n):
    i=1
    sum=0
    while i<n:
        if n%i==0:
            sum+=i
            i+=1
        else:
            i+=1
    return(sum)
print(sum_div(3))
print(sum_div(36))
