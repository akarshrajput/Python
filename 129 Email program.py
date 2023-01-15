def full_emails(people):
    result=[]
    for name,email in people:
        result.append("{} <{}>".format(name,email))
    return result
print(full_emails([("Akarsh","akarsh@gmail.com")]))
print(full_emails([("Sujal","sujal@gmail.com")]))