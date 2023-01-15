import string
punctuations=string.punctuation
str=input("Enter the string: ")
answer=""
for i in str:
    if i in punctuations:
        answer+=i
print(answer)