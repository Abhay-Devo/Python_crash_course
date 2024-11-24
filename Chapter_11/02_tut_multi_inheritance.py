# This is multiple inheritance meaning child class will take inheritance from two or more base classes




class employee:            # Base class 1
    company = "ITC"
    name = "default name"
    def details(self):
        print(f"The name of the employee is: {self.name}, and its company is: {self.company}. ")



class coder:                # Base class 2
    language = "Python"

    def show_lang(self):
        print(f"The default language for every coder is: {self.language}")



# Programmer class gets the inheritance of employee class, 
# means whatever is in the employee now will be in programmer class.

class programmer(employee, coder):      # Derived/Child class
    company2 = "ITC infotech"

    # Other methods diff from employee class.
    def show_company(self):
        print(f"The name of the company is: {self.company2}, and He knows multiple languages.")


a = employee()
c = coder()
b = programmer()


print(f"{a.company}, {b.company}, {b.company2}, {c.language}")
b.details()
b.show_company()
b.show_lang()