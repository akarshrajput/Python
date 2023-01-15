import string
punctuations=string.punctuation
str=input("Enter the string: ")
answer=""
for i in str:
    if i not in punctuations:
        answer+=i
print(answer)