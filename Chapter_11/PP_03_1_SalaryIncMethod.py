# Calculate the new salary after the increment 


# Salary and increment are object attribute
class employee:

    def __init__(self, salary, Inc) -> None:
        self.salary = salary
        self.Inc = Inc
        self.TotalSalary = salary

    @property
    def salaryIncMethod(self):
        return self.TotalSalary
    
    @salaryIncMethod.setter
    def salaryIncMethod(self, value):
        self.TotalSalary = value + (value * (self.Inc/100))

e1 = employee(234, 20)
e1.salaryIncMethod = e1.salary

e2 = employee(10000, 10)
e2.salaryIncMethod = e2.salary

print(f"The total salary after increment of employee 2 is: {e2.salaryIncMethod}")
print(f"The total salary after increment of employee 1 is: {e1.salaryIncMethod}")



# OTHER WAY OF DOING THIS(MORE EFFICIENT)........



# Salary and increment are class attribute and uses more simple logic 
class employee2:

    salary = 10000
    Inc = 10

    @property
    def salaryIncMethod(self):
        return (self.salary + (self.salary * ( self.Inc/100)))  

e1 = employee2()
print(f"The total salary after increment is: {e1.salaryIncMethod}")
