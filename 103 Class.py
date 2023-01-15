class Laptop:
    company=None
    model=None
    def get_info(self):
        company="HP"
        model="Notebook"
        return company+" and "+model
HP=Laptop()
print(HP.get_info())