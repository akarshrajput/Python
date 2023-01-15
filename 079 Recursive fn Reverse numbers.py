def reverse(num):
    if num >5:
        return
    reverse(num+1)
    print(num)
reverse(1)