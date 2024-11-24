# Calcutate the new salary from the old salary after increment in @property(getter decorator)
# Calculate the increment on the new salary from the older one in setter decorator


class employee:
    salary = 234
    inc = 20
    
    @property
    def salaryincmethod(self):
        return (self.salary + (self.salary * (self.inc/100)))
    
    @salaryincmethod.setter
    def salaryincmethod(self, salary):
        self.inc = ((salary/self.salary) -1)*100
        
    
e1 = employee()

print(e1.salaryincmethod)  # uses @property method to calculate the new salary after increment

e1.salaryincmethod = 280.8   # uses @setter method  to calculate increment from old salary to new salary
print(e1.inc)