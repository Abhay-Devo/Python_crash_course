# Inheritance is a way of creating a new class from an existing class.
# This is single inheritance.

class employee:            # Base class
    company = "ITC"

    def __init__(self, name, salary,):
        self.name = name
        self.salary = salary

    def details(self):
        print(f"The name of the employee is: {self.name}, and its salary is: {self.salary}. ")



# Programmer class gets the inheritance of employee class, 
# means whatever is in the employee now will be in programmer class.

class programmer(employee):      # Derived/Child class
    company2 = "ITC infotech"

    # Other methods diff from employee class.
    def show_lang(self):
        print(f"The name of the employee is: {self.company}, and He knows multiple languages.")


a = employee("Harry", 120000)
b = programmer("Rohan", 100000)

print(f"{a.company}, {b.company}, {b.company2}")